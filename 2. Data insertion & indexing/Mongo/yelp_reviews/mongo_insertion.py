# import libraries
import pandas as pd
import sys, getopt, pprint
import pymongo
from pymongo import MongoClient
import csv
import json
import time

# starting time
start_time = time.time()

# program body starts
# CSV to JSON Conversion
csvfile = open('../../data/yelp_review/yelp_review500.csv', 'r', encoding='utf8')
reader = csv.DictReader(csvfile, delimiter=',')
mongo_client=MongoClient() 
db=mongo_client.yelp_review
db.segment.drop()
header= ["review_id","review"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.yelp_review500.insert_one(row)
# program body ends

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

# total time taken
print(f"Runtime of the program is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")