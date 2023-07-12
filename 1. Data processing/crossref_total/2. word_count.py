# import libraries
import pandas

# load the dataset
dataset = pandas.read_csv('/Users/GeoFot/data/crossref_total/crossref_total500.csv', delimiter = ',')
dataset.head()

# fetch wordcount
dataset['word_count'] = dataset['abstract'].apply(lambda x: len(str(x).split(" ")))   # title
dataset[['abstract','word_count']].head()   # title

# descriptive statistics of word counts
df = dataset.word_count.describe()
print(df)