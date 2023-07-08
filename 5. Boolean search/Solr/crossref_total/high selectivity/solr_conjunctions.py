# import libraries
import urllib.request
from urllib.request import urlopen
import time

# starting time
start_time = time.time()

connection = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Adata%20AND%20title%3Apapers)%20OR%20(abstract%3Adata%20AND%20abstract%3Apapers)&wt=python')
response = eval(connection.read())
print (response['response']['numFound'], "documents found")
connection2 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Asecondary%20AND%20title%3Asystems)%20OR%20(abstract%3Asecondary%20AND%20abstract%3Asystems)&wt=python')
response2 = eval(connection2.read())
print (response2['response']['numFound'], "documents found")
connection3 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Asystematic%20AND%20title%3Ameasures)%20OR%20(abstract%3Asystematic%20AND%20abstract%3Ameasures)&wt=python')
response3 = eval(connection3.read())
print (response3['response']['numFound'], "documents found")
connection4 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Anew%20AND%20title%3Apapers)%20OR%20(abstract%3Anew%20AND%20abstract%3Apapers)&wt=python')
response4 = eval(connection4.read())
print (response4['response']['numFound'], "documents found")
connection5 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Amodeling%20AND%20title%3Agroup)%20OR%20(abstract%3Amodeling%20AND%20abstract%3Agroup)&wt=python')
response5 = eval(connection5.read())
print (response5['response']['numFound'], "documents found")
connection6 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Apatients%20AND%20title%3Atemperature)%20OR%20(abstract%3Apatients%20AND%20abstract%3Atemperature)&wt=python')
response6 = eval(connection6.read())
print (response6['response']['numFound'], "documents found")
connection7 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Ablack%20AND%20title%3Ahole)%20OR%20(abstract%3Ablack%20AND%20abstract%3Ahole)&wt=python')
response7 = eval(connection7.read())
print (response7['response']['numFound'], "documents found")
connection8 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Arecent%20AND%20title%3Apapers)%20OR%20(abstract%3Arecent%20AND%20abstract%3Apapers)&wt=python')
response8 = eval(connection8.read())
print (response8['response']['numFound'], "documents found")
connection9 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Acompared%20AND%20title%3Areviews)%20OR%20(abstract%3Acompared%20AND%20abstract%3Areviews)&wt=python')
response9 = eval(connection9.read())
print (response9['response']['numFound'], "documents found")
connection10 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Asearch%20AND%20title%3Apapers)%20OR%20(abstract%3Asearch%20AND%20abstract%3Apapers)&wt=python')
response10 = eval(connection10.read())
print (response10['response']['numFound'], "documents found")

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

# total time taken
print(f"Runtime of the query is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")