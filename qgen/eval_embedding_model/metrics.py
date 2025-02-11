import logging
import numpy as np
from collections import OrderedDict

logger = logging.getLogger(__name__)


class Metric:
    def __init__(self):
        self.core = {}

    def update(self, experiment_result: dict):
        for metric, value in experiment_result.items():
            if metric not in self.core:
                self.core[metric] = []
            self.core[metric].append(value)

    def __repr__(self):
        results = OrderedDict()
        for metric in self.core:
            avg = 0.0
            if len(self.core[metric]) > 0:
                avg = sum(self.core[metric]) / len(self.core[metric])
            results[metric] = avg

        output = []
        for k, v in results.items():
            output.append(f"{k} {v}")
        output = "\n".join(output)

        return output


def hit_at_k(retrieved_items, relevant_items, k):
    """
    Calculate Hit@k
    """
    # k = min(k, len(relevant_items))
    retrieved_at_k = retrieved_items[:k]
    for item in retrieved_at_k:
        if item in relevant_items:
            return 1.0
    return 0.0


def precision_at_k(retrieved_items, relevant_items, k):
    """
    Calculate Precision@k
    """
    # k = min(k, len(relevant_items))
    retrieved_at_k = retrieved_items[:k]
    relevant_at_k = [item for item in retrieved_at_k if item in relevant_items]
    return len(relevant_at_k) / k


def recall_at_k(retrieved_items, relevant_items, k):
    """
    Calculate Recall@k
    """
    # k = min(k, len(relevant_items))
    retrieved_at_k = retrieved_items[:k]
    relevant_at_k = [item for item in retrieved_at_k if item in relevant_items]
    return len(relevant_at_k) / len(relevant_items)


def average_precision_at_k(retrieved_items, relevant_items, k):
    """
    Calculate Average Precision@k (AP@k)
    """
    # k = min(k, len(relevant_items))
    retrieved_at_k = retrieved_items[:k]
    relevant_at_k = [item for item in retrieved_at_k if item in relevant_items]

    if not relevant_at_k:
        return 0.0

    precision_sum = 0.0
    for i, item in enumerate(retrieved_at_k):
        if item in relevant_items:
            precision_sum += len(
                [it for it in retrieved_at_k[: i + 1] if it in relevant_items]
            ) / (i + 1)

    return precision_sum / len(relevant_at_k)


def ndcg_at_k(retrieved_items, relevant_items, k):
    """
    Calculate NDCG@k
    """

    # k = min(k, len(relevant_items))
    def dcg(items):
        return sum(
            [
                1 / np.log2(i + 2)
                for i, item in enumerate(items)
                if item in relevant_items
            ]
        )

    retrieved_at_k = retrieved_items[:k]
    ideal_at_k = relevant_items[:k]

    dcg_k = dcg(retrieved_at_k)
    idcg_k = dcg(ideal_at_k)

    return dcg_k / idcg_k if idcg_k > 0 else 0.0


def mrr_at_k(retrieved_items, relevant_items, k):
    """
    Calculate MRR@k
    """
    # k = min(k, len(relevant_items))
    retrieved_at_k = retrieved_items[:k]

    # Find the rank of the first relevant item
    rank = 0
    for idx, item in enumerate(retrieved_at_k, start=1):
        if item in relevant_items:
            rank = idx
            break
    return 1.0 / rank if rank > 0 else 0.0


def acc_at_k(retrieved_items, relevant_items, k):
    retrieved_at_k = retrieved_items[:k]
    relevant_at_k = [item for item in retrieved_at_k if item in relevant_items]
    if len(relevant_at_k) == min(k, len(relevant_items)):
        return 1.0
    return 0.0


def evaluate(retrieved, relevant, k):
    # hit = hit_at_k(retrieved, relevant, k)
    # acc = acc_at_k(retrieved, relevant, k)
    # precision = precision_at_k(retrieved, relevant, k)
    recall = recall_at_k(retrieved, relevant, k)
    # ap = average_precision_at_k(retrieved, relevant, k)
    # ndcg = ndcg_at_k(retrieved, relevant, k)
    mrr = mrr_at_k(retrieved, relevant, k)
    return {
        # f"hit@{k}": hit,
        # f"acc@{k}": acc,
        # f"precision@{k}": precision,
        f"recall@{k}": recall,
        # f"map@{k}": ap,
        # f"ndcg@{k}": ndcg,
        f"mrr@{k}": mrr,
    }


def autorag_evaluate(preds, labels, cutoffs=[1, 3, 5, 10]):
    """
    Evaluate MRR and Recall at cutoffs.
    """
    metrics = {}

    # MRR
    mrrs = np.zeros(len(cutoffs))
    for pred, label in zip(preds, labels):
        jump = False
        for i, x in enumerate(pred, 1):
            if x in label:
                for k, cutoff in enumerate(cutoffs):
                    if i <= cutoff:
                        mrrs[k] += 1 / i
                jump = True
            if jump:
                break
    mrrs /= len(preds)
    for i, cutoff in enumerate(cutoffs):
        mrr = mrrs[i]
        metrics[f"MRR@{cutoff}"] = mrr

    # Recall
    recalls = np.zeros(len(cutoffs))
    for pred, label in zip(preds, labels):
        for k, cutoff in enumerate(cutoffs):
            # recall = np.intersect1d(label, pred[:cutoff])
            recall = [1 for item in label if item in pred[:cutoff]]
            recalls[k] += len(recall) / len(label)
    recalls /= len(preds)
    for i, cutoff in enumerate(cutoffs):
        recall = recalls[i]
        metrics[f"Recall@{cutoff}"] = recall
    output = []
    for k, v in metrics.items():
        output.append(f"{k} {v}")
    return "\n".join(output)
