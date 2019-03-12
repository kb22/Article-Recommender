import string
from gensim import corpora

import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
# nltk.download('stopwords')
# nltk.download('wordnet')

class Cleaner:

  def __init__(self):
    # Punctuations and stopwords
    self.punctuation = set(string.punctuation)
    self.stoplist = set(stopwords.words('english'))

    # LDA
    self.dictionary = corpora.Dictionary()
    self.lemma = WordNetLemmatizer()

  def remove_punctuation(self, text):
      return ''.join([char for char in text if char not in self.punctuation])


  def remove_numbers(self, text):
      return ''.join([char for char in text if not char.isdigit()])


  def remove_stopwords(self, text):
      return ' '.join([word for word in text.split() if word not in self.stoplist])


  def remove_single_chars(self, text):
      return ' '.join([word for word in text.split() if len(word) > 1])


  def lemmatize(self, text):
      return ' '.join([self.lemma.lemmatize(word) for word in text.split()])


  def clean_text(self, text):
      text = text.replace('\n', '')
      text = self.remove_punctuation(text)
      text = self.remove_numbers(text)
      text = self.remove_stopwords(text)
      text = self.remove_single_chars(text)
      text = self.lemmatize(text)
      return text
