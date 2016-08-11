#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#
import psycopg2
import sys

k1 = int(sys.argv[1])
k2 = int(sys.argv[2])


try:
	conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
	print "Database connected successfully"
except:
	print "unable to connect the database"

cur = conn.cursor()

cur.execute( "SELECT * FROM Tweetwordcount where count >= %d and count <= %d ORDER BY word asc" % (k1, k2) )
rows = cur.fetchall()
print "Word \t Total Number of Occurances (range is between %d to %d)" %(k1, k2)
print "--------------------------------------------------------------------"
for row in rows:
	print "\"%s\" \t\t\t %d" %(row[0], row[1])
conn.close()
