#!/usr/bin/python
import MySQLdb
import operator

def getPostDataFrom():
	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="nathan",  # your password
                     db="politics")        # name of the data base


	# you must create a Cursor object. It will let
	#  you execute all the queries you need
	cur = db.cursor()
	# Use all the SQL you like
	cur.execute("SELECT * FROM post;")
	# print all the first cell of all the rows
	dates={}
	numPosts=0
	for row in cur.fetchall():
		#print row
		
		date=row[3]
 		if not date==None:
 			numPosts+=1
			print date
   			dates.setdefault(date,[])
   			
			postText=row[11]
			textoComplete=row[12]
			#if "video" in url:
			#print "ES VIDEO"
			url=row[10]
			print postText
			print textoComplete
			print url
   			#break
   	print numPosts


getPostDataFrom()
#sorted_dates = sorted(dates.items(), key=operator.itemgetter(0),reverse=True)
#for d,v in sorted_dates:
#	print d

    #break
