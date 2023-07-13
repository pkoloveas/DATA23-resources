# import libraries
import csv
import psycopg2
import time

# connect to postgres db
conn = psycopg2.connect(user="postgres", password="ds123", dbname="yelp_review", host="localhost", port="5432")

# open a cursor to perform database operations
cur = conn.cursor()

copy_sql = """
           COPY yelp_review500 FROM stdin WITH CSV HEADER
           DELIMITER as ','
           """
# starting time
start_time = time.time()

# program body starts
with open('../../data/yelp_review/yelp_review500.csv', 'r', encoding = 'utf-8') as f:
    #next(f) # skip the header row.
    cur.copy_expert(sql=copy_sql, file=f)
# program body ends

# end time
end_time = time.time()

# close the cursor
conn.commit()
cur.close()
conn.close() 

count = (end_time - start_time)
msecs = (count * 1000)

# total time taken
print(f"Runtime of the program is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")