# import libraries
import urllib.request
from urllib.request import urlopen
import time

# starting time
start_time = time.time()

connection = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3Aproport*%20OR%20abstract%3Aproport*&wt=python')
response = eval(connection.read())
print (response['response']['numFound'], "documents found")
connection2 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3Acard*%20OR%20abstract%3Acard*&wt=python')
response2 = eval(connection2.read())
print (response2['response']['numFound'], "documents found")
connection3 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3Abiologi*%20OR%20abstract%3Abiologi*&wt=python')
response3 = eval(connection3.read())
print (response3['response']['numFound'], "documents found")
connection4 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3Alearn*%20OR%20abstract%3Alearn*&wt=python')
response4 = eval(connection4.read())
print (response4['response']['numFound'], "documents found")
connection5 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3Aalgorith*%20OR%20abstract%3Aalgorith*&wt=python')
response5 = eval(connection5.read())
print (response5['response']['numFound'], "documents found")
connection6 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3Adetectio*%20OR%20abstract%3Adetectio*&wt=python')
response6 = eval(connection6.read())
print (response6['response']['numFound'], "documents found")
connection7 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3Aframewo*%20OR%20abstract%3Aframewo*&wt=python')
response7 = eval(connection7.read())
print (response7['response']['numFound'], "documents found")
connection8 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3Asurger*%20OR%20abstract%3Asurger*&wt=python')
response8 = eval(connection8.read())
print (response8['response']['numFound'], "documents found")
connection9 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3Asystemati*%20OR%20abstract%3Asystemati*&wt=python')
response9 = eval(connection9.read())
print (response9['response']['numFound'], "documents found")
connection10 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3Ainflam*%20OR%20abstract%3Ainflam*&wt=python')
response10 = eval(connection10.read())
print (response10['response']['numFound'], "documents found")

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

# total time taken
print(f"Runtime of the query is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")