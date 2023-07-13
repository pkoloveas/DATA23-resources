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
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ phraseto_tsquery('possible differences')")
res = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ phraseto_tsquery('early studies')")
res2 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ phraseto_tsquery('simulation methods')")
res3 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ phraseto_tsquery('next phase')")
res4 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ phraseto_tsquery('following tests')")
res5 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ phraseto_tsquery('single test')")
res6 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ phraseto_tsquery('specific values')")
res7 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ phraseto_tsquery('specific methods')")
res8 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ phraseto_tsquery('same characteristics')")
res9 = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM crossref_total500 WHERE document @@ phraseto_tsquery('small reduction')")
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