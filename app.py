import math
import re
from collections import Counter
from flask import Flask, render_template, request

app = Flask(__name__)

# --- 1. THE CORPUS (Your Database) ---
DOCUMENTS = {
    "Doc 1 (NLP Basics)": "Natural language processing is a subfield of linguistics, computer science, and artificial intelligence.",
    "Doc 2 (Search Engines)": "Search engines use algorithms to rank documents based on relevance to a user's query.",
    "Doc 3 (TF-IDF Def)": "TF-IDF stands for Term Frequency-Inverse Document Frequency. It is a statistical measure used in NLP.",
    "Doc 4 (AI Trends)": "Artificial intelligence and machine learning are revolutionizing modern computer science.",
    "Doc 5 (Engineering)": "To build a search engine, you need to process text, index it, and calculate similarities using vector mathematics."
}

# --- 2. TF-IDF ENGINE ---
def tokenize(text):
    return re.findall(r'\b[a-z0-9]+\b', text.lower())

class CustomSearchEngine:
    def __init__(self, corpus):
        self.corpus = corpus
        self.vocab = set()
        self.doc_tokens = {}
        self.df = Counter()
        self.tf_idf_matrix = {}
        self.num_docs = len(corpus)
        self._build_index()

    def _build_index(self):
        for doc_id, text in self.corpus.items():
            tokens = tokenize(text)
            self.doc_tokens[doc_id] = tokens
            unique_tokens = set(tokens)
            self.vocab.update(unique_tokens)
            for token in unique_tokens:
                self.df[token] += 1

        for doc_id, tokens in self.doc_tokens.items():
            tf_counts = Counter(tokens)
            doc_len = len(tokens)
            self.tf_idf_matrix[doc_id] = {}
            for token, count in tf_counts.items():
                tf = count / doc_len
                idf = math.log((1 + self.num_docs) / (1 + self.df[token])) + 1 
                self.tf_idf_matrix[doc_id][token] = tf * idf

    def search(self, query):
        query_tokens = tokenize(query)
        if not query_tokens:
            return []

        query_counts = Counter(query_tokens)
        query_len = len(query_tokens)
        query_vector = {}

        for token, count in query_counts.items():
            if token in self.vocab:
                tf = count / query_len
                idf = math.log((1 + self.num_docs) / (1 + self.df[token])) + 1
                query_vector[token] = tf * idf

        results = []
        query_norm = math.sqrt(sum(val**2 for val in query_vector.values()))

        for doc_id, doc_vector in self.tf_idf_matrix.items():
            dot_product = 0
            doc_norm = math.sqrt(sum(val**2 for val in doc_vector.values()))
            for token, q_val in query_vector.items():
                if token in doc_vector:
                    dot_product += q_val * doc_vector[token]

            if query_norm > 0 and doc_norm > 0:
                similarity = dot_product / (query_norm * doc_norm)
            else:
                similarity = 0

            if similarity > 0:
                snippet = self.corpus[doc_id]
                results.append({"id": doc_id, "score": round(similarity, 4), "snippet": snippet})

        results.sort(key=lambda x: x['score'], reverse=True)
        return results

engine = CustomSearchEngine(DOCUMENTS)

@app.route('/', methods=['GET', 'POST'])
def home():
    results = []
    query = ""
    if request.method == 'POST':
        query = request.form.get('query', '')
        if query:
            results = engine.search(query)
    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    # Bind to 0.0.0.0 so it is accessible outside the Docker container
    app.run(host='0.0.0.0', port=5000, debug=True)
