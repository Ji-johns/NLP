import nltk
from nltk.corpus import wordnet
import random
import re


# --- Part 1: Replace a word with a synonym ---
sentence = "The quick brown fox jumps over the lazy dog."
word = "quick"

print("Original Sentence:", sentence)

tokens = nltk.word_tokenize(sentence)
synonyms = []

for synset in wordnet.synsets(word):
    for synonym in synset.lemmas():
        synonyms.append(synonym.name())

# Remove duplicates
synonyms = list(set(synonyms))


new_sentence = ""
for token in tokens:
    if token == word and synonyms:
        new_sentence += random.choice(synonyms) + " "
    else:
        new_sentence += token + " "

print("New Sentence:", new_sentence)
print()



text = "This is a sample text with some words to be replaced. Another line with words"
print("Original Text:", text)

regex = r"\b(sample)\b"
replacement = "hello"

new_text = re.sub(regex, replacement, text)
print("Modified Text:", new_text)

