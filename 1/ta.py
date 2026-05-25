import nltk

# Downloads



from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Example sentence
example = "Stop words are words that you want to ignore"

# Tokenization
words = word_tokenize(example)

# Stopwords
stop_word = set(stopwords.words("english"))

# Remove stopwords
filtered_list = []
for word in words:
    if word.casefold() not in stop_word:
        filtered_list.append(word)

print("Filtered words:", filtered_list)

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_list]
print("Stemmed words:", stemmed_words)

# POS Tagging
pos_tags = nltk.pos_tag(filtered_list)
print("POS Tags:", pos_tags)




