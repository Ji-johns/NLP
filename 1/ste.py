import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Example sentence
example = "Stemming is a text processing task in which you reduce words to their root"

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

