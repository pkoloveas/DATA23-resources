# import libraries
import pandas

# load the dataset
dataset = pandas.read_csv('/Users/GeoFot/data/yelp_review/yelp_review500.csv', delimiter = ',')
dataset.head()

# fetch wordcount
dataset['word_count'] = dataset['review'].apply(lambda x: len(str(x).split(" ")))
dataset[['review','word_count']].head()

# descriptive statistics of word counts
df = dataset.word_count.describe()
print(df)