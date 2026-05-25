import nltk
text = "This is the text we'll use to count how many times the word 'the' appears. The more the merrier!"

words = nltk.word_tokenize(text)
count = words.count("the")
print("The word 'the' appears", count, "times in the text.")


