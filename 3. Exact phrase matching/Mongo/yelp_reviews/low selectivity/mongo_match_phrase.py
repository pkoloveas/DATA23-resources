# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["yelp_review"]
mycol=mydb["yelp_review500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.count_documents({"$text": {"$search":"\"really good\""}})]
res2 = [mycol.count_documents({"$text": {"$search":"\"next time\""}})]
res3 = [mycol.count_documents({"$text": {"$search":"\"pretty good\""}})]
res4 = [mycol.count_documents({"$text": {"$search":"\"great place\""}})]
res5 = [mycol.count_documents({"$text": {"$search":"\"great service\""}})]
res6 = [mycol.count_documents({"$text": {"$search":"\"every time\""}})]
res7 = [mycol.count_documents({"$text": {"$search":"\"great food\""}})]
res8 = [mycol.count_documents({"$text": {"$search":"\"ice cream\""}})]
res9 = [mycol.count_documents({"$text": {"$search":"\"good food\""}})]
res10 = [mycol.count_documents({"$text": {"$search":"\"happy hour\""}})]
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