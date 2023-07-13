# import libraries
import psycopg2
import time

# connect to postgres db
conn = psycopg2.connect(user="postgres", password="", dbname="yelp_review", host="localhost", port="5432")

# open a cursor to perform database operations
cur = conn.cursor()

# starting time
start_time = time.time()

# program body starts
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('sta:*')")
res = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('grea:*')")
res2 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('ver:*')")
res3 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('servic:*')")
res4 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('rea:*')")
res5 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('tim:*')")
res6 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('ever:*')")
res7 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('get:*')")
res8 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('lik:*')")
res9 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('some:*')")
res10 = cur.fetchone()
# program body ends

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

result = [res, res2, res3, res4, res5, res6, res7, res8, res9, res10]
for x in result:
    print(x , "records found")

# total time taken
print(f"Runtime of the query is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")

# close the cursor
conn.commit()
cur.close()
conn.close() 