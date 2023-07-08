# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["crossref_total"]
mycol=mydb["crossref_total500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.count_documents({"$text": {"$search":"\"results indicate\""}})]
res2 = [mycol.count_documents({"$text": {"$search":"\"significant differences\""}})]
res3 = [mycol.count_documents({"$text": {"$search":"\"electron microscopy\""}})]
res4 = [mycol.count_documents({"$text": {"$search":"\"control group\""}})]
res5 = [mycol.count_documents({"$text": {"$search":"\"experimental results\""}})]
res6 = [mycol.count_documents({"$text": {"$search":"\"paper presents\""}})]
res7 = [mycol.count_documents({"$text": {"$search":"\"well known\""}})]
res8 = [mycol.count_documents({"$text": {"$search":"\"wide range\""}})]
res9 = [mycol.count_documents({"$text": {"$search":"\"growth factor\""}})]
res10 = [mycol.count_documents({"$text": {"$search":"\"new species\""}})]
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