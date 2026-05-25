import nltk

# Download required NLTK resources
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')

text = "John works for Google in New York"

# Tokenization
tokens = nltk.word_tokenize(text)

# POS tagging
tagged = nltk.pos_tag(tokens)

# Named Entity Recognition (NER)
entities = nltk.ne_chunk(tagged)

# Extract named entities
for entity in entities:
    if hasattr(entity, 'label'):
        print(entity.label(), ' '.join(c[0] for c in entity.leaves()))

