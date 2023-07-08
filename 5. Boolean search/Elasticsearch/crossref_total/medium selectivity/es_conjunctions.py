# import libraries
from elasticsearch import Elasticsearch
import time

es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

# starting time
start_time = time.time()

# program body starts
res = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "different"}},{"match":{"title": "species"}}]}},{"bool":{"must":[{"match":{"abstract": "different"}},{"match": {"abstract": "species"}}]}}]}}},request_timeout=2000)
res2 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "clinical"}},{"match":{"title": "activity"}}]}},{"bool":{"must":[{"match":{"abstract": "clinical"}},{"match": {"abstract": "activity"}}]}}]}}},request_timeout=2000)
res3 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "patient"}},{"match":{"title": "cases"}}]}},{"bool":{"must":[{"match":{"abstract": "patient"}},{"match": {"abstract": "cases"}}]}}]}}},request_timeout=2000)
res4 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "potential"}},{"match":{"title": "risk"}}]}},{"bool":{"must":[{"match":{"abstract": "potential"}},{"match": {"abstract": "risk"}}]}}]}}},request_timeout=2000)
res5 =es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "patients"}},{"match":{"title": "show"}}]}},{"bool":{"must":[{"match":{"abstract": "patients"}},{"match": {"abstract": "show"}}]}}]}}},request_timeout=2000)
res6 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "new"}},{"match":{"title": "test"}}]}},{"bool":{"must":[{"match":{"abstract": "new"}},{"match": {"abstract": "test"}}]}}]}}},request_timeout=2000)
res7 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "negative"}},{"match":{"title": "effects"}}]}},{"bool":{"must":[{"match":{"abstract": "negative"}},{"match": {"abstract": "effects"}}]}}]}}},request_timeout=2000)
res8 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "new"}},{"match":{"title": "cases"}}]}},{"bool":{"must":[{"match":{"abstract": "new"}},{"match": {"abstract": "cases"}}]}}]}}},request_timeout=2000)
res9 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "model"}},{"match":{"title": "difference"}}]}},{"bool":{"must":[{"match":{"abstract": "model"}},{"match": {"abstract": "difference"}}]}}]}}},request_timeout=2000)
res10 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query": {"bool":{"should":[{"bool":{"must":[{"match":{"title": "use"}},{"match":{"title": "tests"}}]}},{"bool":{"must":[{"match":{"abstract": "use"}},{"match": {"abstract": "tests"}}]}}]}}},request_timeout=2000)
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