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
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('filet & table')")
res = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('pizza & water')")
res2 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('filet & first')")
res3 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('sushi & water')")
res4 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('steak & cook')")
res5 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('bloody & bar')")
res6 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('oil & bar')")
res7 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('mignon & steak')")
res8 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('pizza & steak')")
res9 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM yelp_review500 WHERE document @@ to_tsquery('filet & butter')")
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