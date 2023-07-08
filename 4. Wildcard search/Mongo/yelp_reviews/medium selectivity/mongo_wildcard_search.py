# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["yelp_review"]
mycol=mydb["yelp_review500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.find({"review": {"$regex":"sever.*", '$options':'i'}}).count()]
res2 = [mycol.find({"review": {"$regex":"wron.*", '$options':'i'}}).count()]
res3 = [mycol.find({"review": {"$regex":"stat.*", '$options':'i'}}).count()]
res4 = [mycol.find({"review": {"$regex":"fis.*", '$options':'i'}}).count()]
res5 = [mycol.find({"review": {"$regex":"comm.*", '$options':'i'}}).count()]
res6 = [mycol.find({"review": {"$regex":"rese.*", '$options':'i'}}).count()]
res7 = [mycol.find({"review": {"$regex":"brough.*", '$options':'i'}}).count()]
res8 = [mycol.find({"review": {"$regex":"lad.*", '$options':'i'}}).count()]
res9 = [mycol.find({"review": {"$regex":"shrim.*", '$options':'i'}}).count()]
res10 = [mycol.find({"review": {"$regex":"expen.*", '$options':'i'}}).count()]
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