# import libraries
import pandas as pd

# split dataset into batches
chunk_size = 500000
batch_no = 1

for chunk in pd.read_csv('../../data/crossref_total/crossref_total.csv', chunksize=chunk_size, delimiter=',', encoding = "ISO-8859-1"):
    chunk.to_csv('crossref_total' + str(batch_no) + '.csv', index=False)
    batch_no +=1
