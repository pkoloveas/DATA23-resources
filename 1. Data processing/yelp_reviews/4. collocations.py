# import libraries
import nltk
nltk.download('webtext')
from nltk.corpus import webtext
from nltk.corpus import stopwords
  
# use to find bigrams, which are pairs of words
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

stopset = set(stopwords.words('english'))
filter_stops = lambda w: len(w) < 3 or w in stopset

words = [w.lower() for w in webtext.words(r'/Users/GeoFot/data/yelp_review/yelp_review500.csv')]
  
biagram_collocation = BigramCollocationFinder.from_words(words)

biagram_collocation.apply_word_filter(filter_stops)
output = biagram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 100)

print(output)