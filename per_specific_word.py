import nltk
text = "This is the text we'll use to count how many times the word 'the' appears. The more the merrier!"

target_word = "the"
words = nltk.word_tokenize(text)
word_count = words.count(target_word)
total_words =len(words)
precentage = (word_count/total_words)*100

print("The word '" + target_word + "' appears", word_count, "times in the text.")
print("This is", precentage, "% of all the words in the text.")
