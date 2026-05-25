import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
example = "Stop words are words that you want to ignore."
from nltk.corpus import stopwords
stop_word = set(stopwords.words("english"))
words = word_tokenize(example)
filtered_list = []
for word in words:
	if word.casefold() not in stop_word:
		filtered_list.append(word)
print(filtered_list)

