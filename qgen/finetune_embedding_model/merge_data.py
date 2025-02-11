import argparse
from ..utils import read_jsonl, write_jsonl 
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser() 
    parser.add_argument('-g', '--gold_data', type=str)
    parser.add_argument('-s', '--synthetic_data', type=str)
    parser.add_argument('-o', '--output_path', type=str)
    parser.add_argument('-b', '--batch_size', type=int, default=100)
    parser.add_argument('-e', '--n_epochs', type=int, default=1)
    parser.add_argument('--seed', type=int, default=42)

    args = parser.parse_args()

    gold_data = read_jsonl(args.gold_data)
    synthetic_data = read_jsonl(args.synthetic_data)
    output_path = args.output_path 

    print(f"Len gold data: {len(gold_data)}")
    print(f"Len synthetic data: {len(synthetic_data)}")

    n_epochs = args.n_epochs 
    bs = args.batch_size

    bs = min(bs, len(gold_data), len(synthetic_data))

    if len(gold_data) < len(synthetic_data):
        random.seed(args.seed)
        new_gold_data = []
        r = (len(synthetic_data) + len(gold_data) - 1) // len(gold_data)
        for _ in range(r):
           random.shuffle(gold_data)
           new_gold_data.extend(list(gold_data)) 
        gold_data = new_gold_data[:len(synthetic_data)]
            
    ratio = (len(gold_data) + len(synthetic_data) - 1) // len(synthetic_data)
    new_data = []
    random.seed(args.seed)
    for _ in range(n_epochs):
        random.shuffle(synthetic_data)
        random.shuffle(gold_data)

        n_batch = (len(synthetic_data) + bs - 1) // bs
        for i in range(n_batch):
            gold_start_idx = i * bs * ratio
            gold_end_idx = min(gold_start_idx + bs * ratio, len(gold_data)) 
            syn_start_idx = i * bs
            syn_end_idx = min(len(synthetic_data), syn_start_idx + bs)

            new_data.extend(list(synthetic_data[syn_start_idx:syn_end_idx]))
            new_data.extend(list(gold_data[gold_start_idx:gold_end_idx]))


    print(f"Len new data: {len(new_data)}")
    write_jsonl(new_data, output_path)
