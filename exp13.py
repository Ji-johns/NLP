import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text_list):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()

    filtered_sentences = []
    for sentence in text_list:
        tokens = word_tokenize(sentence.lower())
        filtered = [ps.stem(word) for word in tokens
                    if word not in stop_words and word.isalpha()]
        filtered_sentences.append(' '.join(filtered))

    return filtered_sentences


sentences = [
    "The food is tasty",
    "the quality of food is low",
    "i will never recommend their food",
    "I got sick after having thier food",
    "I was in cloudnine after tasting their food",
    "My favourite is their desserts",
    "the food was not cooked properly"
]

classes = [1, 0, 0, 0, 1, 1, 0]

test_sentences = [
    "food is not cooked properly",
    "I feel sick after having food",
    "I love their desserts",
    "I was in cloudnine after tasting their food"
]

vectorizer = CountVectorizer()

sentences = preprocess(sentences)
X_train = vectorizer.fit_transform(sentences)

model = LogisticRegression()
model.fit(X_train, classes)

test_sentences = preprocess(test_sentences)
X_test = vectorizer.transform(test_sentences)

pred_classes = model.predict(X_test)

print(pred_classes)
