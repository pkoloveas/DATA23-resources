# import libraries
from elasticsearch import helpers, Elasticsearch
import csv
import time

# program body starts
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# starting time
start_time = time.time()

with open('../../data/yelp_review/yelp_review500.csv', 'r', encoding='iso-8859-1') as outfile:
    reader = csv.DictReader(outfile, delimiter=',')
    helpers.bulk(es, reader, index='yelp500', doc_type='doc', request_timeout=2000)
# program body ends

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

# total time taken
print(f"Runtime of the program is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")