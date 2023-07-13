# import libraries
import psycopg2
import time

# connect to your postgres DB
conn = psycopg2.connect(user="postgres", password="", dbname="crossref_total", host="localhost", port="5432")

# open a cursor to perform database operations
cur = conn.cursor()

# starting time
start_time = time.time()

# program body starts
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('this & paper')")
res = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('research & of')")
res2 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('patients & results')")
res3 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('the & role')")
res4 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('used & at')")
res5 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('significant & results')")
res6 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('patients & at')")
res7 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('using & data')")
res8 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('significant & study')")
res9 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('clinical & results')")
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