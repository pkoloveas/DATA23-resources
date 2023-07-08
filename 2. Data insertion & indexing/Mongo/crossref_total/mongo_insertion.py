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
csvfile = open('/Users/GeoFot/data/Datasets/crossref_total/crossref_total500.csv', 'r', encoding='utf8')
reader = csv.DictReader(csvfile, delimiter=',')
mongo_client=MongoClient() 
db=mongo_client.crossref_total
db.segment.drop()
header= ["title","abstract"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.crossref_total500.insert_one(row)
# program body ends

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

# total time taken
print(f"Runtime of the program is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")