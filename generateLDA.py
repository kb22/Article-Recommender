# Import libraries
import sqlite3
import pickle
import yaml

from gensim import corpora, utils, models, similarities
from collections import defaultdict

# Import modules
from Modules.Content import Content

# Load configuration
with open('config.yml') as fp:
    config = yaml.load(fp)
fp.close()

# Basic passes
NUM_PASSES = 10
NUM_TOPICS = 100
RANDOM_STATE = 1

# Database and other resources
DATABASE_PATH = config['paths']['database']
LDA_PATH = config['paths']['lda']
DICTIONARY_PATH = config['paths']['dictionary']
CORPUS_PATH = config['paths']['corpus']

# Execution
content = Content(DATABASE_PATH)
dictionary = corpora.Dictionary(content)
# Remove words that appear less than 5 times and that are in more than in 80% documents
dictionary.filter_extremes(no_below=5, no_above=0.8)
corpus = [dictionary.doc2bow(text) for text in content]

# LDA Model
lda = models.LdaModel(corpus, id2word=dictionary, random_state=RANDOM_STATE,
                      num_topics=NUM_TOPICS, passes=NUM_PASSES)

# Save resources
lda.save(LDA)
with open(DICTIONARY, 'wb') as fp:
    pickle.dump(dictionary, fp)
fp.close()
with open(CORPUS, 'wb') as fp:
    pickle.dump(corpus, fp)
fp.close()
