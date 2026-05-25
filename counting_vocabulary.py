import nltk


text="This is a sample text to count the number of the words. It contains multiple sentences and punctuations."

words = nltk.word_tokenize(text)
num_words = len(words)
print("The number of the words(tokens) in the text is:", num_words)


