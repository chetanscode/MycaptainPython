import random
import pandas as pd
from nltk.util import ngrams
# Sample corpus containing poetry
poetry_corpus =pd.read_csv('PoetryFoundationData.csv')

poetry_corpus.head()
poetry_corpus.shape
corpus_po=""
for i in range(200):
    
    corpus_po=corpus_po+"\n"+poetry_corpus['Poem'][i]
  corpus=corpus_po


# Tokenize the text into words
from nltk.tokenize import word_tokenize

words = nltk.word_tokenize(corpus)

# Create a bigram model
bigram_model = list(ngrams(words, 2))

# Generate poetry with a specified number of words per line
def generate_poem(words_per_line, num_lines=5):
    poem = []
    start_word = random.choice(words)
    for _ in range(num_lines):
        line = [start_word]
        current_word = start_word
        while len(line) < words_per_line:
            next_word = [word for word in bigram_model if word[0] == current_word]
            if not next_word:
                break
            next_word = random.choice(next_word)[1]
            line.append(next_word)
            current_word = next_word
        poem.append(" ".join(line))
    return "\n".join(poem)

# Generate poetry with 8 words per line
words_per_line = 8
generated_poem = generate_poem(words_per_line)
print(generated_poem)
