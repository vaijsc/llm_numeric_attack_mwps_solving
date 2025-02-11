import argparse
import os
import sys

import torch
from ..indices.faiss_index import FaissFlatIPIndex
from ..models.embedding import EmbeddingModel
from src.utils import (
    dict_to_text,
    prepare_file,
    read_jsonl,
    read_pickle,
    setup_logger,
    write_pickle,
)

from .metrics import Metric, evaluate

logger = setup_logger()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--corpus_path",
        type=str,
        default="",
    )
    parser.add_argument(
        "-q", "--query_path", type=str, default=""
    )
    parser.add_argument(
        "-o",
        "--output_path",
        type=str,
        default="",
    )
    parser.add_argument(
        "-e",
        "--embedding_model_path",
        type=str,
        default="",
    )
    parser.add_argument(
        "-t",
        "--model_type",
        type=str,
        default="bge-m3",
    )
    parser.add_argument(
        "--context_embedding_save_path",
        type=str,
        default="",
    )
    parser.add_argument(
        "--query_embedding_save_path",
        type=str,
        default="",
    )
    parser.add_argument("-b", "--embedding_batch_size", type=int, default=32)
    parser.add_argument("--max_length", type=int, default=1024)
    parser.add_argument("-br", "--retrieve_batch_size", type=int, default=32)
    parser.add_argument("--use_gpu", action='store_true', default=False)
    parser.add_argument(
        "-r",
        "--result_path",
        type=str,
        default="",
    )
    parser.add_argument("-k", "--top_k", type=int, default=10)
    parser.add_argument("--cutoffs", nargs="+", type=int, default=[1, 3, 5, 10])
    return parser.parse_args()


def get_embedding(
    model_path,
    model_type,
    contexts,
    queries,
    batch_size,
    max_length,
    context_embedding_save_path=None,
    query_embedding_save_path=None,
):
    logger.info("Load embedding model")
    encoder = EmbeddingModel(model_path, model_type)

    logger.info("Encode contexts")
    context_embeddings = encoder.encode(
        contexts,
        max_length=max_length,
        batch_size=batch_size,
        save_path=context_embedding_save_path,
    )

    query_texts = [q["query"] for q in queries]
    query_embeddings = encoder.encode(
        query_texts,
        max_length=max_length,
        batch_size=batch_size,
        save_path=query_embedding_save_path,
    )
    torch.cuda.empty_cache()
    return context_embeddings, query_embeddings


def evaluate_retrival(retrieval_output, cutoffs, result_path=None):
    results = Metric()
    for obj in retrieval_output:
        retrieved_items = obj["preds"]
        relevant_items = obj["pos"]
        for k in cutoffs:
            results.update(evaluate(retrieved_items, relevant_items, k))
    logger.info(f"Results:\n{results}\n")
    if result_path:
        prepare_file(result_path)
        with open(result_path, "w") as fout:
            fout.write(f"Results:\n{results}\n")
            fout.write("\n")
        logger.info(f"Save results to `{result_path}`")


def main():
    args = get_args()
    logger.info(f"Config:\n{dict_to_text(vars(args), sort=True)}")

    if os.path.isfile(args.output_path):
        logger.info("Evaluate output")
        evaluate_retrival(
            read_pickle(args.output_path, verbose=False), args.cutoffs, args.result_path
        )
        sys.exit(0)

    # Read data
    logger.info("Read data")
    contexts = read_jsonl(args.corpus_path)
    page_nums = [f"doc_{c['doc_name']}_page_{int(c['page_num'])}" for c in contexts]
    contexts = [c["content"] for c in contexts]
    logger.info(f"Total {len(contexts)} contexts")

    queries = read_jsonl(args.query_path)
    queries = [{"query": q['query'], "pos": [f"doc_{c['doc_name']}_page_{int(c['page_num'])}" for c in q['evidences']] } for q in queries]
    logger.info(f"Total {len(queries)} queries")

    context_embeddings, query_embeddings = get_embedding(
        args.embedding_model_path,
        args.model_type,
        contexts,
        queries,
        args.embedding_batch_size,
        args.max_length,
        args.context_embedding_save_path,
        args.query_embedding_save_path,
    )

    logger.info("Retrieve contexts")
    dim = context_embeddings.shape[-1]
    index = FaissFlatIPIndex(dim, use_gpu=args.use_gpu)
    index.add_vectors(context_embeddings)
    scores, indices = index.search(
        query_embeddings, top_k=args.top_k, batch_size=args.retrieve_batch_size
    )

    logger.info("Evaluate output")
    retrieval_output = []
    for query, idxs, score in zip(queries, indices, scores):
        retrieved_items = [page_nums[idx] for idx in idxs]
        retrieval_output.append(
            {**query, "preds": retrieved_items, "pred_scores": score}
        )
    if args.output_path:
        write_pickle(retrieval_output, args.output_path)

    evaluate_retrival(retrieval_output, args.cutoffs, args.result_path)


if __name__ == "__main__":
    main()
