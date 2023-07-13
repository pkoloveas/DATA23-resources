# import libraries
import psycopg2
import time

# connect to postgres db
conn = psycopg2.connect(user="postgres", password="", dbname="crossref_total", host="localhost", port="5432")

# open a cursor to perform database operations
cur = conn.cursor()

# starting time
start_time = time.time()

# program body starts
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('proport:*')")
res = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('card:*')")
res2 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('biologi:*')")
res3 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('learn:*')")
res4 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('algorith:*')")
res5 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('detectio:*')")
res6 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('framewo:*')")
res7 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('surger:*')")
res8 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('systemati:*')")
res9 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ to_tsquery('inflam:*')")
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