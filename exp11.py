import nltk
nltk.download('brown')
nltk.download('punkt')

from nltk.corpus import brown
from nltk.tag import hmm

def train_hmm_tagger():
    tagged_sentences = brown.tagged_sents(categories='news')

    size = int(len(tagged_sentences) * 0.9)
    train_sents = tagged_sentences[:size]
    test_sents = tagged_sentences[size:]

    trainer = hmm.HiddenMarkovModelTrainer()

    hmm_tagger = trainer.train_supervised(train_sents)

    print("Accuracy:", hmm_tagger.evaluate(test_sents))

    return hmm_tagger


def pos_tag_sentence(sentence, hmm_tagger):
    tokens = nltk.word_tokenize(sentence)
    return hmm_tagger.tag(tokens)


hmm_tagger = train_hmm_tagger()

sentence = input("Enter the sentence to be tagged: ")
tagged = pos_tag_sentence(sentence, hmm_tagger)

print("\nTagged Sentence:")
for word, tag in tagged:
    print(word, ":", tag)

