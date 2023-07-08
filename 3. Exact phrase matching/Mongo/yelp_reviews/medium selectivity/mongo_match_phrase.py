# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["yelp_review"]
mycol=mydb["yelp_review500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.count_documents({"$text": {"$search":"\"peanut butter\""}})]
res2 = [mycol.count_documents({"$text": {"$search":"\"oil change\""}})]
res3 = [mycol.count_documents({"$text": {"$search":"\"nice atmosphere\""}})]
res4 = [mycol.count_documents({"$text": {"$search":"\"filet mignon\""}})]
res5 = [mycol.count_documents({"$text": {"$search":"\"bloody mary\""}})]
res6 = [mycol.count_documents({"$text": {"$search":"\"foie gras\""}})]
res7 = [mycol.count_documents({"$text": {"$search":"\"nice people\""}})]
res8 = [mycol.count_documents({"$text": {"$search":"\"sushi bar\""}})]
res9 = [mycol.count_documents({"$text": {"$search":"\"super clean\""}})]
res10 = [mycol.count_documents({"$text": {"$search":"\"cooked well\""}})]
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