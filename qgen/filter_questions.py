import argparse
import json
import logging
import os
import pickle

import faiss

from .models.embedding import EmbeddingModel
from .utils import prepare_file, setup_logger, write_jsonl

logger = logging.getLogger(__name__)


class QuestionFilter:
    """Select hiquality questions base on similarity score on a corpus of contexts"""

    def __init__(
        self,
        model_path,
        input_path,
        candidate_path=None,
        question_embeddings_save_path=None,
        context_embeddings_save_path=None,
        score_save_path=None,
        batch_size=16,
        top_k: int = 10,
        use_gpu=False,
    ) -> None:
        self.model_path = model_path
        self.input_path = input_path
        self.candidate_path = candidate_path
        self.top_k = top_k
        self.question_embeddings_save_path = question_embeddings_save_path
        self.context_embeddings_save_path = context_embeddings_save_path
        self.score_save_path = score_save_path
        self.batch_size = batch_size
        self.use_gpu = use_gpu

    def _get_data(self):
        self.data = [
            json.loads(line.strip()) for line in open(self.input_path).readlines()
        ]
        self.data = [d for d in self.data if len(d["questions"]) > 0]
        self.contexts = [d["context"] for d in self.data]
        self.contexts = list(set(self.contexts))

        # add external candidate to context coprpus
        if self.candidate_path:
            candidates = [
                json.loads(line.strip())
                for line in open(self.candidate_path).readlines()
            ]
            candidates = [d["content"] for d in candidates]
            candidates.extend(self.contexts)
            candidates = list(set(candidates))
            self.contexts = candidates

        logger.info(f"{len(self.contexts)} contexts")

        # convert input triplet (context, question, answer) for easier selection
        self.cqs = []
        for d in self.data:
            for question in d["questions"]:
                self.cqs.append(
                    {
                        "context": d["context"],
                        "question": question,
                    }
                )
        logger.info(f"{len(self.cqs)} CQA triplets")

    def _search_top_k_cosine(self, k: int, Q, C):
        dim = Q.shape[-1]
        index = faiss.IndexFlatIP(dim)
        if self.use_gpu:
            co = faiss.GpuMultipleClonerOptions()
            co.shard = True
            co.useFloat16 = False
            index = faiss.index_cpu_to_all_gpus(index, co=co)
        index.add(C)
        score, indices = index.search(Q, k)
        return score, indices

    def run(self, gold_context_threshold, top_k_threshold):
        self._get_data()

        # check if there is processed score
        if os.path.isfile(self.score_save_path):
            with open(self.score_save_path, "rb") as fin:
                saved = pickle.load(fin)
                self.score = saved['score']
                self.indices = saved['indices']
        else:
            embedding_model = EmbeddingModel(self.model_path)
            self.C = embedding_model.encode(
                self.contexts,
                batch_size=self.batch_size,
                save_path=self.context_embeddings_save_path,
            )
            self.Q = embedding_model.encode(
                [o["question"] for o in self.cqs],
                batch_size=self.batch_size,
                save_path=self.question_embeddings_save_path,
            )

            self.score, self.indices = self._search_top_k_cosine(
                self.top_k, self.Q, self.C
            )
            del self.Q
            del self.C
            if self.score_save_path:
                with open(self.score_save_path, "wb") as fout:
                    pickle.dump({"score": self.score, "indices": self.indices}, fout)


        output = []
        for question_idx, cq in enumerate(self.cqs):
            # k-th context must has score <= t_k threshold
            if self.score[question_idx][-1] > top_k_threshold:
                continue
            # if self.score[question_idx][0] < gold_context_threshold:
            #     continue
            #
            # gold context must be in top k contexts
            retrieved_contexts = [self.contexts[context_idx] for context_idx in self.indices[question_idx]]
            try:
                gold_context_idx = retrieved_contexts.index(cq['context'])
            except ValueError:
                continue

            # gold_context must have score >= t_g threshold
            # if self.score[question_idx][gold_context_idx] < gold_context_threshold:
            #     continue

            output.append(cq)

        return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_path", type=str, default="")
    parser.add_argument("-c", "--candidate_path", type=str, default=None)
    parser.add_argument("--question_embeddings_save_path", type=str, default="")
    parser.add_argument("--context_embeddings_save_path", type=str, default="")
    parser.add_argument("--score_save_path", type=str, default="")
    parser.add_argument("-o", "--output_path", type=str, default="")
    parser.add_argument("-m", "--model_path", type=str, default="")
    parser.add_argument("-k", "--top_k", type=int, default=10)
    parser.add_argument("-b", "--batch_size", type=int, default=16)
    parser.add_argument("--max_question_per_context", type=int, default=2)
    parser.add_argument("--gold_context_threshold", type=float, default=0.6)
    parser.add_argument("--top_k_threshold", type=float, default=0.5)
    parser.add_argument("-g", "--use_gpu", action="store_true", default=False)
    args = parser.parse_args()

    logger = setup_logger()
    for k in sorted(list(vars(args).keys())):
        logger.info(f"{k:10s}: {getattr(args, k)}")

    prepare_file(args.output_path)
    if args.question_embeddings_save_path:
        prepare_file(args.question_embeddings_save_path)
    if args.context_embeddings_save_path:
        prepare_file(args.context_embeddings_save_path)
    if args.score_save_path:
        prepare_file(args.score_save_path)

    question_filter = QuestionFilter(
        model_path=args.model_path,
        input_path=args.input_path,
        candidate_path=args.candidate_path,
        question_embeddings_save_path=args.question_embeddings_save_path,
        context_embeddings_save_path=args.context_embeddings_save_path,
        score_save_path=args.score_save_path,
        batch_size=args.batch_size,
        top_k=args.top_k,
        use_gpu=True,
    )
    output = question_filter.run(args.gold_context_threshold, args.top_k_threshold)

    logger.info("Convert to embedding finetuning data")
    
    idx = 0
    contexts = set([d['context'] for d in output])
    context_2_id = {c:idx for idx, c in enumerate(contexts)}

    dict_data = {}
    for d in output:
        context = d['context']
        if context not in dict_data:
            dict_data[context] = []
        dict_data[context].append(d['question'])
    
    output = []
    for k,v in dict_data.items():
        context = k
        for question in v:
            output.append({ 
                "query": question,
                "pos": [context],
                "neg": [],
            })
    write_jsonl(output, args.output_path)
    logger.info(
        f"Gold context threshold: {args.gold_context_threshold:0.2f} | "
        f"Top {args.top_k} threshold: {args.top_k_threshold} | "
        f"{len(output)} CQ pairs"
    )
    logger.info(f"Save data to {args.output_path}")
