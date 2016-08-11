#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#
import psycopg2
import sys

if ( len(sys.argv) == 2 ):
	input = str(sys.argv[1])


try:
	conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
	print "Database connected"
except:
	print "Unable to connect the database"

cur = conn.cursor()

if ( len(sys.argv) == 2 ):
	query = "SELECT * FROM Tweetwordcount where word = %s"
	cur.execute( "SELECT * FROM Tweetwordcount where word = '%s'" % (input) )
	rows = cur.fetchall()
	print "Word \t Total Number of Occurances"
	print "--------------------------------------------------------------------"
	for row in rows:
		print "\"%s\"\t\t\t %d" %(row[0], row[1])
	conn.close()
else:
	query = "SELECT * FROM Tweetwordcount ORDER BY word"
	cur.execute(query)
	rows = cur.fetchall()
	print "Word \t Number of Occurances"
	print "--------------------------------------------------------------------"
	for row in rows:
		print "\"%s\"\t\t\t %d" %(row[0], row[1])
	conn.close()

