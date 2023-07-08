# import libraries
import urllib.request
from urllib.request import urlopen
import time

# starting time
start_time = time.time()

connection = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3A%22system%20based%22%20OR%20abstract%3A%22system%20based%22&wt=python')
response = eval(connection.read())
print (response['response']['numFound'], "documents found")
connection2 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3A%22negative%20effects%22%20OR%20abstract%3A%22negative%20effects%22&wt=python')
response2 = eval(connection2.read())
print (response2['response']['numFound'], "documents found")
connection3 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3A%22study%20results%22%20OR%20abstract%3A%22study%20results%22&wt=python')
response3 = eval(connection3.read())
print (response3['response']['numFound'], "documents found")
connection4 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3A%22clinical%20activity%22%20OR%20abstract%3A%22clinical%20activity%22&wt=python')
response4 = eval(connection4.read())
print (response4['response']['numFound'], "documents found")
connection5 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3A%22different%20species%22%20OR%20abstract%3A%22different%20species%22&wt=python')
response5 = eval(connection5.read())
print (response5['response']['numFound'], "documents found")
connection6 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3A%22potential%20risk%22%20OR%20abstract%3A%22potential%20risk%22&wt=python')
response6 = eval(connection6.read())
print (response6['response']['numFound'], "documents found")
connection7 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3A%22research%20studies%22%20OR%20abstract%3A%22research%20studies%22&wt=python')
response7 = eval(connection7.read())
print (response7['response']['numFound'], "documents found")
connection8 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3A%22increased%20number%22%20OR%20abstract%3A%22increased%20number%22&wt=python')
response8 = eval(connection8.read())
print (response8['response']['numFound'], "documents found")
connection9 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3A%22first%20group%22%20OR%20abstract%3A%22first%20group%22&wt=python')
response9 = eval(connection9.read())
print (response9['response']['numFound'], "documents found")
connection10 = urlopen('http://localhost:8983/solr/crossref_total500/select?q=title%3A%22high%20number%22%20OR%20abstract%3A%22high%20number%22&wt=python')
response10 = eval(connection10.read())
print (response10['response']['numFound'], "documents found")

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

# total time taken
print(f"Runtime of the query is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")