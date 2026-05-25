from sklearn.feature_extraction.text import CountVectorizer
documents = [
"This is the first this document.",
"This is the second document with some overlap.",
"This is the third document with new information."
]

# Create the Bag of Words model
vectorizer = CountVectorizer()

# Fit the model on the preprocessed documents
bow_model = vectorizer.fit_transform(documents)

# Print the vocabulary
print("Vocabulary:", vectorizer.get_feature_names_out())

# Print the Bag of Words representation for each document
print("Bag of Words:")

for i in range(0,len(documents)):
	print(f"{documents[i]}:\n {bow_model.toarray()[i]}")
