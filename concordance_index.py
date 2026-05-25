import nltk
from nltk.tokenize import word_tokenize
from nltk.text import ConcordanceIndex

# Download required tokenizer data (run once)
#nltk.download('punkt_tab')

example_string = (
    "Now that you’re up to speed on parts of speech, you can circle back "
    "to lemmatizing. Like stemming, lemmatizing reduces words to their core meaning"
)

tokens = word_tokenize(example_string.lower())

conc = ConcordanceIndex(tokens)
conc.print_concordance('speed')

