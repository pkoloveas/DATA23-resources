# import libraries
from elasticsearch import Elasticsearch
import time

es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

# starting time
start_time = time.time()

# program body starts
res = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "this"}},{"match":{"title": "paper"}}]}},{"bool":{"must":[{"match":{"abstract": "this"}},{"match": {"abstract": "paper"}}]}}]}}},request_timeout=2000)
res2 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "research"}},{"match":{"title": "of"}}]}},{"bool":{"must":[{"match":{"abstract": "research"}},{"match": {"abstract": "of"}}]}}]}}},request_timeout=2000)
res3 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "patients"}},{"match":{"title": "results"}}]}},{"bool":{"must":[{"match":{"abstract": "patients"}},{"match": {"abstract": "results"}}]}}]}}},request_timeout=2000)
res4 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "the"}},{"match":{"title": "role"}}]}},{"bool":{"must":[{"match":{"abstract": "the"}},{"match": {"abstract": "role"}}]}}]}}},request_timeout=2000)
res5 =es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "used"}},{"match":{"title": "at"}}]}},{"bool":{"must":[{"match":{"abstract": "used"}},{"match": {"abstract": "at"}}]}}]}}},request_timeout=2000)
res6 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "significant"}},{"match":{"title": "results"}}]}},{"bool":{"must":[{"match":{"abstract": "significant"}},{"match": {"abstract": "results"}}]}}]}}},request_timeout=2000)
res7 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "patients"}},{"match":{"title": "at"}}]}},{"bool":{"must":[{"match":{"abstract": "patients"}},{"match": {"abstract": "at"}}]}}]}}},request_timeout=2000)
res8 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "using"}},{"match":{"title": "data"}}]}},{"bool":{"must":[{"match":{"abstract": "using"}},{"match": {"abstract": "data"}}]}}]}}},request_timeout=2000)
res9 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "significant"}},{"match":{"title": "study"}}]}},{"bool":{"must":[{"match":{"abstract": "significant"}},{"match": {"abstract": "study"}}]}}]}}},request_timeout=2000)
res10 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "clinical"}},{"match":{"title": "results"}}]}},{"bool":{"must":[{"match":{"abstract": "clinical"}},{"match": {"abstract": "results"}}]}}]}}},request_timeout=2000)
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