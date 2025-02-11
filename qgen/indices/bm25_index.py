import bm25s
import Stemmer

class BM25Index:
    def __init__(self, stopwords="en", language="english"):
        """
        Initialize the BM25 index with optional stopwords and stemming.
        """
        self.retriever = bm25s.BM25()
        self.corpus = []
        self.stemmer = Stemmer.Stemmer(language) if language else None
        self.stopwords = stopwords
        self.indexed = False

    def add_contexts(self, contexts, output_path=None):
        """
        Add contexts (documents) to the BM25 index and tokenize them.
        
        Parameters:
        - contexts: A list of text documents to add to the corpus.
        """
        # Tokenize the new contexts
        context_tokens = bm25s.tokenize(contexts, stopwords=self.stopwords, stemmer=self.stemmer)
        # Append new contexts to the existing corpus
        self.corpus.extend(contexts)
        # Index the corpus
        self.retriever.index(context_tokens)
        self.indexed = True

        if output_path:
            self.save(output_path)

    def search(self, query, corpus=None, k=2):
        """
        Search the indexed corpus for the most similar documents to the query.

        Parameters:
        - query: The search query (string).
        - k: The number of top results to return.

        Returns:
        - A list of tuples containing (document, score) for the top-k results.
        """
        if not self.indexed:
            raise ValueError("The corpus has not been indexed yet. Add contexts first.")

        if isinstance(query, str) and not query.strip():
            return [], []
        if isinstance(query, list) and not query[0].strip():
            return [], []

        # Tokenize the query
        query_tokens = bm25s.tokenize(query, stemmer=self.stemmer)

        # Make sure k does not exceed the number of documents
        if not corpus:
            corpus = self.corpus
        k = min(k, len(corpus))

        # Retrieve top-k results
        docs, scores = self.retriever.retrieve(query_tokens, corpus=corpus, k=k)
        return scores, docs
        # Prepare the result as (document, score) tuples
        # ranked_results = [(doc, score) for doc, score in zip(results[0], scores[0])]

        # return ranked_results

    def save(self, path):
        """
        Save the BM25 model and the corpus to a file.
        
        Parameters:
        - path: The file path to save the model and corpus.
        """
        self.retriever.save(path, corpus=self.corpus)

    def load(self, path):
        """
        Load the BM25 model and the corpus from a file.
        
        Parameters:
        - path: The file path to load the model and corpus from.
        """
        self.retriever = bm25s.BM25.load(path, load_corpus=True)
        # When loading, the corpus may be in a dictionary with 'text' fields
        self.corpus = [doc['text'] if isinstance(doc, dict) else doc for doc in self.retriever.corpus]
        self.indexed = True
