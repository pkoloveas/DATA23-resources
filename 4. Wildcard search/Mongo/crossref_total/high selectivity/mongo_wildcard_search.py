# import libraries
import pymongo
import time

client=pymongo.MongoClient()
mydb=client["crossref_total"]
mycol=mydb["crossref_total500"]

# starting time
start_time = time.time()

# program body starts
res = [mycol.find({ "$or": [{"title": {"$regex":"dendrit.*", '$options':'i'}}, {"abstract": {"$regex":"dendrit.*", '$options':'i'}}]}).count()]
res2 = [mycol.find({ "$or": [{"title": {"$regex":"disparit.*", '$options':'i'}}, {"abstract": {"$regex":"disparit.*", '$options':'i'}}]}).count()]
res3 = [mycol.find({ "$or": [{"title": {"$regex":"trigl.*", '$options':'i'}}, {"abstract": {"$regex":"trigl.*", '$options':'i'}}]}).count()]
res4 = [mycol.find({ "$or": [{"title": {"$regex":"hepatit.*", '$options':'i'}}, {"abstract": {"$regex":"hepatit.*", '$options':'i'}}]}).count()]
res5 = [mycol.find({ "$or": [{"title": {"$regex":"atheroscler.*", '$options':'i'}}, {"abstract": {"$regex":"atheroscler.*", '$options':'i'}}]}).count()]
res6 = [mycol.find({ "$or": [{"title": {"$regex":"irreve.*", '$options':'i'}}, {"abstract": {"$regex":"irreve.*", '$options':'i'}}]}).count()]
res7 = [mycol.find({ "$or": [{"title": {"$regex":"vaccinat.*", '$options':'i'}}, {"abstract": {"$regex":"vaccinat.*", '$options':'i'}}]}).count()]
res8 = [mycol.find({ "$or": [{"title": {"$regex":"arthrit.*", '$options':'i'}}, {"abstract": {"$regex":"arthrit.*", '$options':'i'}}]}).count()]
res9 = [mycol.find({ "$or": [{"title": {"$regex":"synop.*", '$options':'i'}}, {"abstract": {"$regex":"synop.*", '$options':'i'}}]}).count()]
res10 = [mycol.find({ "$or": [{"title": {"$regex":"osteop.*", '$options':'i'}}, {"abstract": {"$regex":"osteop.*", '$options':'i'}}]}).count()]
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