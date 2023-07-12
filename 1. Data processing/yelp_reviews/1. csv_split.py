# import libraries
import pandas as pd

# split dataset into batches
chunk_size = 500000
batch_no = 1

for chunk in pd.read_csv('/Users/GeoFot/data/yelp_review/yelp_review.csv', chunksize=chunk_size, delimiter=','):
    chunk.to_csv('yelp_review' + str(batch_no) + '.csv', index=False)
    batch_no +=1