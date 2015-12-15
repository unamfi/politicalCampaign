#!/usr/bin/python
import MySQLdb
import operator
import pickle

def getNumPhotosVideoShared():
   videoKeywords={}
   videoKeywords["periscope"]=0
   videoKeywords["mobile uploads"]=0
   videoKeywords["photo"]=0
   videoKeywords["video"]=0

   urlKeywords={}
   urlKeywords["video"]=0
   urlKeywords["periscope"]=0
   urlKeywords["soundcloud"]=0
   urlKeywords["thinglink"]=0
   urlKeywords["photo"]=0
   urlKeywords["youtu.be"]=0
   urlKeywords["youtube"]=0
   urlKeywords["/transmisiones/envivo.aspx"]=0
   urlKeywords["ustream"]=0
   urlKeywords["libre/players/mmplayer"]=0
   urlKeywords["ustream"]=0
   urlKeywords["ustream"]=0
   urlKeywords["/envivo"]=0
   urlKeywords["audiolive"]=0
   
   numPostsVideo=0
   totalPosts=0
   dates = pickle.load(open("postsDates.p", "rb"))
   FILE=open("trash.txt",'w')
   tiposTotales={}
   for d in dates:
      #print d
      tipoPosts=dates[d]
      for t in tipoPosts:
         tiposTotales.setdefault(t,0)
         tiposTotales[t]+=len(tipoPosts[t])
         tLower=t.lower()
         foundItsMedia=False
         for keyword in videoKeywords:
            if keyword in tLower:
               #print "Found:"+t
               numPostsVideo+=len(tipoPosts[t])
               totalPosts+=len(tipoPosts[t])
               foundItsMedia=True
               break
         if not foundItsMedia:
            print "Not found:"+t
            FILE.write("Tipo:"+str(t)+"\n************\n")
            urls=tipoPosts[t]
            for u in urls:
               u=u.lower()
               foundKeyordUrl=False
               for keywordU in  urlKeywords:
                  if keywordU in u:
                     foundKeyordUrl=True
                     #numPostsVideo+=1
                     print "..actually i found something:"+str(u)
                     break
               if foundKeyordUrl:
                  numPostsVideo+=1
                  totalPosts+=1
               else:
                  
                  FILE.write(u+"\n")
                  totalPosts+=1
         FILE.write("\n")
   print numPostsVideo
   print totalPosts
   percentageFotos=getPercentage(totalPosts, numPostsVideo)
   print "Percentage Fotos:"+str(percentageFotos)
   FILE.close()

def getPercentage(total, indivAmount):
   indivAmount=indivAmount*100
   indivAmount=float(float(indivAmount)/float(total))
   return indivAmount






         #print t
         #if "photo" in t:
          #  print t
   #print
   #print
   #FILE=open("trash.txt",'w')
   #for t in tiposTotales:
    #  print t
      #FILE.write(t+"\n")
   #FILE.close()
   #pickle.dump(dates, open("postsDates.p", "wb"))

def getDatesPost():
   db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="nathan",  # your password
                     db="politics")        # name of the data base
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
         
         #print date
         tipoPost=row[11]
         texto=row[12]
         url=row[10]
            
         if not tipoPost==None:
            dates.setdefault(date,{})
            dates[date].setdefault(tipoPost,{})
            dates[date][tipoPost][url]=texto
            #print tipoPost
            #print texto
            #print url
            numPosts+=1
            #print
         
   print numPosts
   pickle.dump(dates, open("postsDates.p", "wb"))
   #pickle.dump(dates,"postsDates.p")
   sorted_dates = sorted(dates.items(), key=operator.itemgetter(0),reverse=True)
   tipoPostsCount={}
      
   for d,v in sorted_dates:
      
      tipoPosts=dates[d]
      for t in tipoPosts:

         tipoPostsCount.setdefault(t,0)
         tipoPostsCount[t]+=1
         
   sorted_tipoPostsCount = sorted(tipoPostsCount.items(), key=operator.itemgetter(1),reverse=True)
   m=0
   for t,v in sorted_tipoPostsCount:
      if m<20:
         print t+","+str(v)
      else:
         break
      m+=1
   print d




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
			
   	print numPosts
   	sorted_dates = sorted(dates.items(), key=operator.itemgetter(0),reverse=True)
   	
   	tipoPostsCount={}
   	
   	for d,v in sorted_dates:
   	
   		tipoPosts=dates[d]
   		for t in tipoPosts:

   			tipoPostsCount.setdefault(t,0)
   			tipoPostsCount[t]+=1
   		
   	sorted_tipoPostsCount = sorted(tipoPostsCount.items(), key=operator.itemgetter(1),reverse=True)
   	m=0
   	for t,v in sorted_tipoPostsCount:
   		if m<20:
   			print t+","+str(v)
   		else:
   			break
   		m+=1
      #print numPosts
      #print numPosts
   		



#getPostDataFrom()
#getDatesPost()
getNumPhotosVideoShared()

#sorted_dates = sorted(dates.items(), key=operator.itemgetter(0),reverse=True)
#for d,v in sorted_dates:
#	print d

    #break
