# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["crossref_total"]
mycol=mydb["crossref_total500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.count_documents({"$text": {"$search":"\"different\" \"species\""}})]
res2 = [mycol.count_documents({"$text": {"$search":"\"clinical\" \"activity\""}})]
res3 = [mycol.count_documents({"$text": {"$search":"\"patient\" \"cases\""}})]
res4 = [mycol.count_documents({"$text": {"$search":"\"potential\" \"risk\""}})]
res5 = [mycol.count_documents({"$text": {"$search":"\"patients\" \"show\""}})]
res6 = [mycol.count_documents({"$text": {"$search":"\"new\" \"test\""}})]
res7 = [mycol.count_documents({"$text": {"$search":"\"negative\" \"effects\""}})]
res8 = [mycol.count_documents({"$text": {"$search":"\"new\" \"cases\""}})]
res9 = [mycol.count_documents({"$text": {"$search":"\"model\" \"difference\""}})]
res10 = [mycol.count_documents({"$text": {"$search":"\"use\" \"tests\""}})]
# program body ends

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

result = [res, res2, res3, res4, res5, res6, res7, res8, res9, res10]
for x in result:
    print(x , "documents found")

# total time taken
print(f"Runtime of the query is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")