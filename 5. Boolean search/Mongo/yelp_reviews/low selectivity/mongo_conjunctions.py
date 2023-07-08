# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["yelp_review"]
mycol=mydb["yelp_review500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.count_documents({"$text": {"$search":"\"great\" \"place\""}})]
res2 = [mycol.count_documents({"$text": {"$search":"\"great\" \"food\""}})]
res3 = [mycol.count_documents({"$text": {"$search":"\"good\" \"service\""}})]
res4 = [mycol.count_documents({"$text": {"$search":"\"great\" \"service\""}})]
res5 = [mycol.count_documents({"$text": {"$search":"\"would\" \"be\""}})]
res6 = [mycol.count_documents({"$text": {"$search":"\"good\" \"time\""}})]
res7 = [mycol.count_documents({"$text": {"$search":"\"really\" \"good\""}})]
res8 = [mycol.count_documents({"$text": {"$search":"\"go\" \"back\""}})]
res9 = [mycol.count_documents({"$text": {"$search":"\"first\" \"time\""}})]
res10 = [mycol.count_documents({"$text": {"$search":"\"pretty\" \"good\""}})]
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