# import libraries
import urllib.request
from urllib.request import urlopen
import time

# starting time
start_time = time.time()

connection = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Athis%20AND%20title%3Apaper)%20OR%20(abstract%3Athis%20AND%20abstract%3Apaper)&wt=python')
response = eval(connection.read())
print (response['response']['numFound'], "documents found")
connection2 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Aresearch%20AND%20title%3Aof)%20OR%20(abstract%3Aresearch%20AND%20abstract%3Aof)&wt=python')
response2 = eval(connection2.read())
print (response2['response']['numFound'], "documents found")
connection3 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Apatients%20AND%20title%3Aresults)%20OR%20(abstract%3Apatients%20AND%20abstract%3Aresults)&wt=python')
response3 = eval(connection3.read())
print (response3['response']['numFound'], "documents found")
connection4 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Athe%20AND%20title%3Arole)%20OR%20(abstract%3Athe%20AND%20abstract%3Arole)&wt=python')
response4 = eval(connection4.read())
print (response4['response']['numFound'], "documents found")
connection5 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Aused%20AND%20title%3Aat)%20OR%20(abstract%3Aused%20AND%20abstract%3Aat)&wt=python')
response5 = eval(connection5.read())
print (response5['response']['numFound'], "documents found")
connection6 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Asignificant%20AND%20title%3Aresults)%20OR%20(abstract%3Asignificant%20AND%20abstract%3Aresults)&wt=python')
response6 = eval(connection6.read())
print (response6['response']['numFound'], "documents found")
connection7 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Apatients%20AND%20title%3Aat)%20OR%20(abstract%3Apatients%20AND%20abstract%3Aat)&wt=python')
response7 = eval(connection7.read())
print (response7['response']['numFound'], "documents found")
connection8 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Ausing%20AND%20title%3Adata)%20OR%20(abstract%3Ausing%20AND%20abstract%3Adata)&wt=python')
response8 = eval(connection8.read())
print (response8['response']['numFound'], "documents found")
connection9 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Asignificant%20AND%20title%3Astudy)%20OR%20(abstract%3Asignificant%20AND%20abstract%3Astudy)&wt=python')
response9 = eval(connection9.read())
print (response9['response']['numFound'], "documents found")
connection10 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Aclinical%20AND%20title%3Aresults)%20OR%20(abstract%3Aclinical%20AND%20abstract%3Aresults)&wt=python')
response10 = eval(connection10.read())
print (response10['response']['numFound'], "documents found")

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

# total time taken
print(f"Runtime of the query is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")