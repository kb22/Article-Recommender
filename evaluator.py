# Import libraries
import pickle
import yaml
import argparse
from gensim import models, similarities

# Import modules
from Modules.Cleaner import Cleaner
from Modules.Content import Content

# Load configuration
with open('config.yml') as fp:
    config = yaml.load(fp)
fp.close()

# Database and other resources
DATABASE = config['paths']['database']
LDA = config['paths']['lda']
DICTIONARY = config['paths']['dictionary']
CORPUS = config['paths']['corpus']

# Load all respources
with open(DICTIONARY, 'rb') as fp:
    dictionary = pickle.load(fp)
    fp.close()
with open(CORPUS, 'rb') as fp:
    corpus = pickle.load(fp)
    fp.close()
lda = models.LdaModel.load(LDA)


def get_similarity(lda, query_vector):
    index = similarities.MatrixSimilarity(lda[corpus])
    sims = index[query_vector]
    return sims


# Define arguments
parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query', dest='query')
values = parser.parse_args()

# Define variables based on arguments
if (values.query):
    query = values.query
else:
    print('Error: Please enter the string to be searched')
    exit(1)

cleaner = Cleaner()
words = dictionary.doc2bow(cleaner.clean_text(query).split())
print("Top words identified: ")
for word in words:
    print("{} {}".format(word[0], dictionary[word[0]]))

query_vector = lda[words]
sims = get_similarity(lda, query_vector)
sims = sorted(enumerate(sims), key=lambda item: -item[1])

idx = 0
pids = []
result = 10
content = Content(DATABASE)
page_ids = content.get_ids()
print("\nCheck out the links below:")
while result > 0:
    pageid = page_ids[sims[idx][0]]
    if pageid not in pids:
        pids.append(pageid)
        print("{}".format(content.get_url_by_id(pageid)))
        result -= 1
    idx += 1
