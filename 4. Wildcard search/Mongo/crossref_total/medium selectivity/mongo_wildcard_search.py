# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["crossref_total"]
mycol=mydb["crossref_total500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.find({ "$or": [{"title": {"$regex":"proport.*", '$options':'i'}}, {"abstract": {"$regex":"proport.*", '$options':'i'}}]}).count()]
res2 = [mycol.find({ "$or": [{"title": {"$regex":"card.*", '$options':'i'}}, {"abstract": {"$regex":"card.*", '$options':'i'}}]}).count()]
res3 = [mycol.find({ "$or": [{"title": {"$regex":"biologi.*", '$options':'i'}}, {"abstract": {"$regex":"biologi.*", '$options':'i'}}]}).count()]
res4 = [mycol.find({ "$or": [{"title": {"$regex":"learn.*", '$options':'i'}}, {"abstract": {"$regex":"learn.*", '$options':'i'}}]}).count()]
res5 = [mycol.find({ "$or": [{"title": {"$regex":"algorith.*", '$options':'i'}}, {"abstract": {"$regex":"algorith.*", '$options':'i'}}]}).count()]
res6 = [mycol.find({ "$or": [{"title": {"$regex":"detectio.*", '$options':'i'}}, {"abstract": {"$regex":"detectio.*", '$options':'i'}}]}).count()]
res7 = [mycol.find({ "$or": [{"title": {"$regex":"framewo.*", '$options':'i'}}, {"abstract": {"$regex":"framewo.*", '$options':'i'}}]}).count()]
res8 = [mycol.find({ "$or": [{"title": {"$regex":"surger.*", '$options':'i'}}, {"abstract": {"$regex":"surger.*", '$options':'i'}}]}).count()]
res9 = [mycol.find({ "$or": [{"title": {"$regex":"systemati.*", '$options':'i'}}, {"abstract": {"$regex":"systemati.*", '$options':'i'}}]}).count()]
res10 = [mycol.find({ "$or": [{"title": {"$regex":"inflam.*", '$options':'i'}}, {"abstract": {"$regex":"inflam.*", '$options':'i'}}]}).count()]
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