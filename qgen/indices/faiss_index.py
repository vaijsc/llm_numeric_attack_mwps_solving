import faiss
import numpy as np
from faiss import Index


class FaissIndex:
    vector_dimension: int = 0
    use_gpu: bool = False
    index: Index = None

    def add_vectors(self, vectors):
        """
        Add vectors to the index.
        :param vectors: NumPy array of vectors to add to the index.
        """
        if self.use_gpu:
            vectors = np.ascontiguousarray(vectors.astype("float16"))

        self.index.add(vectors)

    def search(self, query_vectors, top_k: float = 5, batch_size=32):
        """
        Perform a vector search and return the top_k closest vectors.
        :param query_vectors: NumPy array of query vectors.
        :param top_k: Number of nearest neighbors to return.
        :param batch_size:
        :return: Tuple of (distances, indices) of the top_k nearest neighbors.
        """
        if self.use_gpu:
            query_vectors = np.ascontiguousarray(query_vectors.astype("float16"))

        indices = []
        scores = []
        # p_bar = tqdm(total=len(queries), desc='Queries', ncols=0)
        L = query_vectors.shape[0]
        for start_idx in range(0, L, batch_size):
            end_idx = min(L, start_idx + batch_size)
            score_, indices_ = self.index.search(
                query_vectors[start_idx:end_idx], top_k
            )
            indices.append(indices_)
            scores.append(score_)
            # p_bar.update(end_idx - start_idx)

        indices = np.concatenate(indices, axis=0)
        scores = np.concatenate(scores, axis=0)
        return scores, indices

    def save_index(self, file_path):
        """
        Save the index to a file.
        :param file_path: Path to save the index file.
        """
        index_cpu = faiss.index_gpu_to_cpu(self.index) if self.use_gpu else self.index
        faiss.write_index(index_cpu, file_path)

    def load_index(self, file_path):
        """
        Load an index from a file.
        :param file_path: Path to the index file.
        """
        index_cpu = faiss.read_index(file_path)
        self.index = (
            faiss.index_cpu_to_gpu(self.res, 0, index_cpu)
            if self.use_gpu
            else index_cpu
        )


class FaissFlatIPIndex(FaissIndex):
    def __init__(self, vector_dimension, use_gpu=True):
        """
        Initialize the Faiss GPU vector search using IndexFlatL2.

        Parameters:
        :param vector_dimension: Dimension of the vectors.
        :param use_gpu: Boolean indicating whether to use GPU (default: True).

        """
        self.vector_dimension = vector_dimension
        self.use_gpu = use_gpu
        self.index = faiss.IndexFlatIP(vector_dimension)  # Flat L2 index

        # If GPU is enabled, move the index to GPU
        if self.use_gpu:
            co = faiss.GpuMultipleClonerOptions()
            co.shard = True
            co.useFloat16 = True
            self.index = faiss.index_cpu_to_all_gpus(self.index, co=co)
