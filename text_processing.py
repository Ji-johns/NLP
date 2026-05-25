import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# ---------------- DOWNLOAD REQUIRED PACKAGES ----------------
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# ---------------- SAMPLE TEXT ----------------
text = "This is a sample text to demonstrate text preprocessing techniques."

# ---------------- 1. TOKENIZATION ----------------
tokens = nltk.word_tokenize(text)
print("Tokenized words:", tokens)

# ---------------- 2. STOP WORD REMOVAL ----------------
stop_words = set(stopwords.words('english'))

stop_removed = []
for word in tokens:
    if word not in stop_words:
        stop_removed.append(word)

print("Built-in Stop words removed:", stop_removed)

# ----------- CUSTOM STOP WORDS ----------------
custom_stop = ["text", "sample"]
stop_words.update(custom_stop)

stop_removed_new = []
for word in tokens:
    if word not in stop_words:
        stop_removed_new.append(word)

print("Custom Stop words removed:", stop_removed_new)

# ---------------- 3. STEMMING ----------------
stemmer = PorterStemmer()
stem_removed = []

for word in stop_removed_new:
    stem_removed.append(stemmer.stem(word))

print("Stemmed words:", stem_removed)

# ---------------- 4. LEMMATIZATION ----------------
text = "Running is fun and playing games is enjoyable."

tokens = nltk.word_tokenize(text)     
pos_tags = nltk.pos_tag(tokens)

lemmatizer = WordNetLemmatizer()
lemmatized_words = ""

for word, tag in pos_tags:
    if tag.startswith('V'):
        pos = 'v'
    elif tag.startswith('N'):
        pos = 'n'
    elif tag.startswith('J'):
        pos = 'a'
    elif tag.startswith('R'):
        pos = 'r'
    else:
        pos = 'n'

    lemmatized_words += lemmatizer.lemmatize(word.lower(), pos) + " "


print("Original text:", text)
print("Lemmatized text:", lemmatized_words)

