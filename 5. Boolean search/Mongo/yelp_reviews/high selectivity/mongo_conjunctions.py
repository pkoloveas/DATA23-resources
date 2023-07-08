# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["yelp_review"]
mycol=mydb["yelp_review500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.count_documents({"$text": {"$search":"\"filet\" \"table\""}})]
res2 = [mycol.count_documents({"$text": {"$search":"\"pizza\" \"water\""}})]
res3 = [mycol.count_documents({"$text": {"$search":"\"filet\" \"first\""}})]
res4 = [mycol.count_documents({"$text": {"$search":"\"sushi\" \"water\""}})]
res5 = [mycol.count_documents({"$text": {"$search":"\"steak\" \"cook\""}})]
res6 = [mycol.count_documents({"$text": {"$search":"\"bloody\" \"bar\""}})]
res7 = [mycol.count_documents({"$text": {"$search":"\"oil\" \"bar\""}})]
res8 = [mycol.count_documents({"$text": {"$search":"\"mignon\" \"steak\""}})]
res9 = [mycol.count_documents({"$text": {"$search":"\"pizza\" \"steak\""}})]
res10 = [mycol.count_documents({"$text": {"$search":"\"filet\" \"butter\""}})]
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