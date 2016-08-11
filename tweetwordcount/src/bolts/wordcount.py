from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
from time import time,ctime

import psycopg2
from redis import StrictRedis
from psycopg2 import connect
import sys

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
		self.counts = Counter()
		self.conn = connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
		self.log("Database connection is closed : ",self.conn.closed)
		self.cur = self.conn.cursor()
		self.redis = StrictRedis()

    def process(self, tup):
		word = tup.values[0]
		self.counts[word] += 1
		if self.counts[word]>1:
			query = "UPDATE tweetwordcount SET count=%s WHERE word=%s;" 
			data = (int(self.counts[word]), str(word) )
			self.cur.execute(query,data)  
			self.conn.commit()
		else:
			query = "INSERT into Tweetwordcount (word, count) SELECT %s, %s WHERE NOT EXISTS (SELECT word from Tweetwordcount Where word = %s);" 
#			query = "INSERT into tweetwordcount (word, count) VALUES (%s,%s);" 
			data = (str(word), 1,str(word))
			self.cur.execute(query,data)  
			self.conn.commit()
			
		self.emit([word, self.counts[word]])
		self.log('%s: %d' % (word, self.counts[word]))
		
		
