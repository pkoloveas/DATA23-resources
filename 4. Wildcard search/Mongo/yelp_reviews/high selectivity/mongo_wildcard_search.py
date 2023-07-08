# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["yelp_review"]
mycol=mydb["yelp_review500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.find({"review": {"$regex":"flower.*", '$options':'i'}}).count()]
res2 = [mycol.find({"review": {"$regex":"celebrati.*", '$options':'i'}}).count()]
res3 = [mycol.find({"review": {"$regex":"friendli.*", '$options':'i'}}).count()]
res4 = [mycol.find({"review": {"$regex":"hooke.*", '$options':'i'}}).count()]
res5 = [mycol.find({"review": {"$regex":"memori.*", '$options':'i'}}).count()]
res6 = [mycol.find({"review": {"$regex":"clothin.*", '$options':'i'}}).count()]
res7 = [mycol.find({"review": {"$regex":"seasonal.*", '$options':'i'}}).count()]
res8 = [mycol.find({"review": {"$regex":"transp.*", '$options':'i'}}).count()]
res9 = [mycol.find({"review": {"$regex":"bedroo.*", '$options':'i'}}).count()]
res10 = [mycol.find({"review": {"$regex":"skeptic.*", '$options':'i'}}).count()]
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