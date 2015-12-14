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
 			
			print date
			tipoPost=row[11]
			texto=row[12]
			url=row[10]
   			
   			if not tipoPost==None:
				dates.setdefault(date,{})
				dates[date].setdefault(tipoPost,{})
				dates[date][tipoPost][url]=texto
				print tipoPost
				print texto
				print url
				numPosts+=1
				print
			#dicionarioPost["tituloPost"]=titlePostText
			#dicionarioPost["texto"]=texto
			#dicionarioPost["url"]=url
   			#break
   	print numPosts
   	sorted_dates = sorted(dates.items(), key=operator.itemgetter(0),reverse=True)
   	#numUrl=0
   	tipoPostsCount={}
   	#i=0
   	for d,v in sorted_dates:
   	#	if i==0:
   	#		print d
   	#	i+=1
   		tipoPosts=dates[d]
   		for t in tipoPosts:

   			tipoPostsCount.setdefault(t,0)
   			tipoPostsCount[t]+=1
   			#print t
   	#		webs=tipoPosts[t]
   	#		for w in webs:
   			#	print w
   	#			numUrl+=1
   	#print d
   	#print numUrl
   	#print numPosts
   	sorted_tipoPostsCount = sorted(tipoPostsCount.items(), key=operator.itemgetter(1),reverse=True)
   	m=0
   	for t,v in sorted_tipoPostsCount:
   		if m<20:
   			print t+","+str(v)
   		else:
   			break
   		m+=1
   		#print t+","
   		#print v
   		#break




getPostDataFrom()
#sorted_dates = sorted(dates.items(), key=operator.itemgetter(0),reverse=True)
#for d,v in sorted_dates:
#	print d

    #break
