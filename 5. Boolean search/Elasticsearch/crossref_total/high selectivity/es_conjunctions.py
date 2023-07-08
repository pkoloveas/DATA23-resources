# import libraries
from elasticsearch import Elasticsearch
import time

es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

# starting time
start_time = time.time()

# program body starts
res = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "data"}},{"match":{"title": "papers"}}]}},{"bool":{"must":[{"match":{"abstract": "data"}},{"match": {"abstract": "papers"}}]}}]}}},request_timeout=2000)
res2 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "secondary"}},{"match":{"title": "systems"}}]}},{"bool":{"must":[{"match":{"abstract": "secondary"}},{"match": {"abstract": "systems"}}]}}]}}},request_timeout=2000)
res3 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "systematic"}},{"match":{"title": "measures"}}]}},{"bool":{"must":[{"match":{"abstract": "systematic"}},{"match": {"abstract": "measures"}}]}}]}}},request_timeout=2000)
res4 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "new"}},{"match":{"title": "papers"}}]}},{"bool":{"must":[{"match":{"abstract": "new"}},{"match": {"abstract": "papers"}}]}}]}}},request_timeout=2000)
res5 =es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "modeling"}},{"match":{"title": "group"}}]}},{"bool":{"must":[{"match":{"abstract": "modeling"}},{"match": {"abstract": "group"}}]}}]}}},request_timeout=2000)
res6 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "patients"}},{"match":{"title": "temperature"}}]}},{"bool":{"must":[{"match":{"abstract": "patients"}},{"match": {"abstract": "temperature"}}]}}]}}},request_timeout=2000)
res7 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "black"}},{"match":{"title": "hole"}}]}},{"bool":{"must":[{"match":{"abstract": "black"}},{"match": {"abstract": "hole"}}]}}]}}},request_timeout=2000)
res8 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "recent"}},{"match":{"title": "papers"}}]}},{"bool":{"must":[{"match":{"abstract": "recent"}},{"match": {"abstract": "papers"}}]}}]}}},request_timeout=2000)
res9 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "compared"}},{"match":{"title": "reviews"}}]}},{"bool":{"must":[{"match":{"abstract": "compared"}},{"match": {"abstract": "reviews"}}]}}]}}},request_timeout=2000)
res10 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "search"}},{"match":{"title": "papers"}}]}},{"bool":{"must":[{"match":{"abstract": "search"}},{"match": {"abstract": "papers"}}]}}]}}},request_timeout=2000)
# program body ends

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

result = [res, res2, res3, res4, res5, res6, res7, res8, res9, res10]
for x in result:
    print(x)

# total time taken
print(f"Runtime of the query is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")