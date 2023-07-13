# import libraries
import urllib.request
from urllib.request import urlopen
import time

# starting time
start_time = time.time()

# program body starts
data = open('../../data/crossref_total/crossref_total500.csv', 'r', encoding='iso-8859-1')
url = 'http://localhost:8983/solr/crossref_total500/update/csv?commit=true&separator=%2C'
req = urllib.request.Request(url, data, {'Content-Type': 'text/plain'})
f = urllib.request.urlopen(req)
for x in f:
    print(x)
f.close()
# program body ends

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

# total time taken
print(f"Runtime of the program is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")