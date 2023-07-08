# import libraries
import urllib.request
from urllib.request import urlopen
import time

# starting time
start_time = time.time()

connection = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Adifferent%20AND%20title%3Aspecies)%20OR%20(abstract%3Adifferent%20AND%20abstract%3Aspecies)&wt=python')
response = eval(connection.read())
print (response['response']['numFound'], "documents found")
connection2 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Aclinical%20AND%20title%3Aactivity)%20OR%20(abstract%3Aclinical%20AND%20abstract%3Aactivity)&wt=python')
response2 = eval(connection2.read())
print (response2['response']['numFound'], "documents found")
connection3 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Apatient%20AND%20title%3Acases)%20OR%20(abstract%3Apatient%20AND%20abstract%3Acases)&wt=python')
response3 = eval(connection3.read())
print (response3['response']['numFound'], "documents found")
connection4 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Apotential%20AND%20title%3Arisk)%20OR%20(abstract%3Apotential%20AND%20abstract%3Arisk)&wt=python')
response4 = eval(connection4.read())
print (response4['response']['numFound'], "documents found")
connection5 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Apatients%20AND%20title%3Ashow)%20OR%20(abstract%3Apatients%20AND%20abstract%3Ashow)&wt=python')
response5 = eval(connection5.read())
print (response5['response']['numFound'], "documents found")
connection6 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Anew%20AND%20title%3Atest)%20OR%20(abstract%3Anew%20AND%20abstract%3Atest)&wt=python')
response6 = eval(connection6.read())
print (response6['response']['numFound'], "documents found")
connection7 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Anegative%20AND%20title%3Aeffects)%20OR%20(abstract%3Anegative%20AND%20abstract%3Aeffects)&wt=python')
response7 = eval(connection7.read())
print (response7['response']['numFound'], "documents found")
connection8 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Anew%20AND%20title%3Acases)%20OR%20(abstract%3Anew%20AND%20abstract%3Acases)&wt=python')
response8 = eval(connection8.read())
print (response8['response']['numFound'], "documents found")
connection9 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Amodel%20AND%20title%3Adifference)%20OR%20(abstract%3Amodel%20AND%20abstract%3Adifference)&wt=python')
response9 = eval(connection9.read())
print (response9['response']['numFound'], "documents found")
connection10 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=(title%3Ause%20AND%20title%3Atests)%20OR%20(abstract%3Ause%20AND%20abstract%3Atests)&wt=python')
response10 = eval(connection10.read())
print (response10['response']['numFound'], "documents found")

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

# total time taken
print(f"Runtime of the query is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")