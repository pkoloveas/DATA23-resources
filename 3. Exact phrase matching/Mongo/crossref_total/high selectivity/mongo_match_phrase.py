# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["crossref_total"]
mycol=mydb["crossref_total500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.count_documents({"$text": {"$search":"\"possible differences\""}})]
res2 = [mycol.count_documents({"$text": {"$search":"\"early studies\""}})]
res3 = [mycol.count_documents({"$text": {"$search":"\"simulation methods\""}})]
res4 = [mycol.count_documents({"$text": {"$search":"\"next phase\""}})]
res5 = [mycol.count_documents({"$text": {"$search":"\"following tests\""}})]
res6 = [mycol.count_documents({"$text": {"$search":"\"single test\""}})]
res7 = [mycol.count_documents({"$text": {"$search":"\"specific values\""}})]
res8 = [mycol.count_documents({"$text": {"$search":"\"specific methods\""}})]
res9 = [mycol.count_documents({"$text": {"$search":"\"same characteristics\""}})]
res10 = [mycol.count_documents({"$text": {"$search":"\"small reduction\""}})]
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