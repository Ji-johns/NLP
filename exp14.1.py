from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Define corpus
corpus = [
    'this is the first document',
    'this is the second document'
]

# 2. Initialize vectorizer
vectorizer = TfidfVectorizer()

# 3. Fit and transform corpus
tfidf_matrix = vectorizer.fit_transform(corpus)

# 4. Compute cosine similarity
similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

# 5. Print result
print("Similarity between documents:", similarity[0][0])
