import nltk
text = "This is a sample text with some repeated words to demonstrate counting uniquewords." 

words = nltk.word_tokenize(text)
unique_words = set(words)
num_unique_words = len(unique_words)
print("The number of unique words (types) in the text is:", num_unique_words)


