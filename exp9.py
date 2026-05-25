import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

line = 'the qick brown fox jump over a lazy dog'

tokens = nltk.word_tokenize(line)

stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

lem = WordNetLemmatizer()
lemmatized_tokens = [lem.lemmatize(token) for token in filtered_tokens]

pos_tags = nltk.pos_tag(lemmatized_tokens)
pos_word_corpus = [(word, tag) for word, tag in pos_tags]

for word, tag in pos_word_corpus:
    print(word, ':', tag)

