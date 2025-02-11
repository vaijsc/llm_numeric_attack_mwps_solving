import argparse
import logging
from .utils import prepare_file, read_jsonl, write_jsonl

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_path", type=str, required=True)
    parser.add_argument("-o", "--output_path", type=str, required=True)
    args = parser.parse_args()

    logger.info("Convert to embedding finetuning data format")

    idx = 0
    data = read_jsonl(args.input_path)
    contexts = set([d["context"] for d in data])
    context_2_id = {c: idx for idx, c in enumerate(contexts)}

    dict_data = {}
    for d in data:
        context = d["context"]
        if context not in dict_data:
            dict_data[context] = [] 
        dict_data[context].extend(d['questions'])
    for k in dict_data:
        dict_data[k] = list(set(dict_data[k]))

    output = []
    for k, v in dict_data.items():
        context = k
        for question in v:
            output.append(
                {
                    "query": question,
                    "pos": [context],
                    "neg": [],
                }
            )
    prepare_file(args.output_path)
    write_jsonl(output, args.output_path)
    logger.info(f"{len(output)} CQ pairs")
    logger.info(f"Save data to {args.output_path}")
