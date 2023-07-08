# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["crossref_total"]
mycol=mydb["crossref_total500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.find({ "$or": [{"title": {"$regex":"mod.*", '$options':'i'}}, {"abstract": {"$regex":"mod.*", '$options':'i'}}]}).count()]
res2 = [mycol.find({ "$or": [{"title": {"$regex":"diffe.*", '$options':'i'}}, {"abstract": {"$regex":"diffe.*", '$options':'i'}}]}).count()]
res3 = [mycol.find({ "$or": [{"title": {"$regex":"effe.*", '$options':'i'}}, {"abstract": {"$regex":"effe.*", '$options':'i'}}]}).count()]
res4 = [mycol.find({ "$or": [{"title": {"$regex":"pat.*", '$options':'i'}}, {"abstract": {"$regex":"pat.*", '$options':'i'}}]}).count()]
res5 = [mycol.find({ "$or": [{"title": {"$regex":"sign.*", '$options':'i'}}, {"abstract": {"$regex":"sign.*", '$options':'i'}}]}).count()]
res6 = [mycol.find({ "$or": [{"title": {"$regex":"prese.*", '$options':'i'}}, {"abstract": {"$regex":"prese.*", '$options':'i'}}]}).count()]
res7 = [mycol.find({ "$or": [{"title": {"$regex":"usi.*", '$options':'i'}}, {"abstract": {"$regex":"usi.*", '$options':'i'}}]}).count()]
res8 = [mycol.find({ "$or": [{"title": {"$regex":"spec.*", '$options':'i'}}, {"abstract": {"$regex":"spec.*", '$options':'i'}}]}).count()]
res9 = [mycol.find({ "$or": [{"title": {"$regex":"dat.*", '$options':'i'}}, {"abstract": {"$regex":"dat.*", '$options':'i'}}]}).count()]
res10 = [mycol.find({ "$or": [{"title": {"$regex":"prop.*", '$options':'i'}}, {"abstract": {"$regex":"prop.*", '$options':'i'}}]}).count()]
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