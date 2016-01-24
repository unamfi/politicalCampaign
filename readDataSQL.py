#!/usr/bin/python
import MySQLdb
import operator
import pickle
import datetime
import csv

def correctCSVComments():
   exampleFile = open('commentsBroncoEdited.csv')
   exampleReader = csv.reader(exampleFile)
   datesRates={}

   for row in exampleReader:
      if exampleReader.line_num>1:
         print exampleReader.line_num
         print row
         date=row[0]
         rate=row[1]
         datesRates[date]=rate
   sorted_dates = sorted(datesRates.items(), key=operator.itemgetter(0),reverse=False)
   FILE=open("commentsBroncoFinal.csv",'w')
   for d,r in sorted_dates:
      print str(d)+","+str(r)
      FILE.write(str(d)+","+str(r)+"\n")
   FILE.close()

         #break
      #print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

def getNumPhotosVideoShared():
   urlsFinal={}
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
   
   tiposTotales={}
   tiposTotalesYear={}


   for d in dates:
      year=d.year
      tiposTotalesYear.setdefault(year,{})
      #print d
      tipoPosts=dates[d]
      for t in tipoPosts:
         tiposTotales.setdefault(t,0)
         tiposTotalesYear[year].setdefault(t,0)
         tiposTotalesYear[year][t]+=len(tipoPosts[t])

         tiposTotales[t]+=len(tipoPosts[t])
         tLower=t.lower()
         foundItsMedia=False
         for keyword in videoKeywords:
            if keyword in tLower:
               #print "Found:"+t
               numPostsVideo+=len(tipoPosts[t])
               totalPosts+=len(tipoPosts[t])
               foundItsMedia=True
               links=tipoPosts[t]
               for l in links:
                  urlsFinal.setdefault(l,0)
                  urlsFinal[l]+=1

               #urlsFinal
               break
         if not foundItsMedia:
            print "Not found:"+t
           # FILE.write("Tipo:"+str(t)+"\n************\n")
            urls=tipoPosts[t]
            for u in urls:
               urlsFinal.setdefault(u,0)
               urlsFinal[u]+=1
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
                  
                  #FILE.write(u+"\n")
                  totalPosts+=1
         #FILE.write("\n")
   print numPostsVideo
   print totalPosts
   percentageFotos=getPercentage(totalPosts, numPostsVideo)
   print "Percentage Fotos:"+str(percentageFotos)
   #pickle.dump(tiposTotales, open("postsDates.p", "wb"))
   #tiposTotales


   #FILE.close()
   #for u in urlsFinal:
   #   print u


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

#pickle.dump(dates, open("postsDates.p", "wb"))

def isMedia(tipo):
   videoKeywords={}
   videoKeywords["periscope"]=0
   videoKeywords["mobile uploads"]=0
   videoKeywords["photo"]=0
   videoKeywords["video"]=0
   videoKeywords["soundcloud"]=0
   videoKeywords["thinglink"]=0
   videoKeywords["photo"]=0
   videoKeywords["youtu.be"]=0
   videoKeywords["youtube"]=0
   videoKeywords["/transmisiones/envivo.aspx"]=0
   videoKeywords["ustream"]=0
   videoKeywords["libre/players/mmplayer"]=0
   videoKeywords["ustream"]=0
   videoKeywords["ustream"]=0
   videoKeywords["/envivo"]=0
   videoKeywords["audiolive"]=0

   for keyword in videoKeywords:
      if keyword in tipo:
         #print "FOund it!:"+str(tipo)
         return True

          #  if keyword in tLower:

def testComments():
   datesPostIds = pickle.load(open("datesPostIDs.p", "rb"))
   postsWithComments = pickle.load(open("postsComments.p", "rb"))
   sorted_dates = sorted(datesPostIds.items(), key=operator.itemgetter(0),reverse=False)
   dates=[]
   X=[]
   x=0

   Y=[]
   for d,posts in sorted_dates:
      print d
      posts=datesPostIds[d]
      for p in posts:
         if p in postsWithComments:
            print "Found Post!"
            print len(postsWithComments[p])
            numComments=len(postsWithComments[p])
            X.append(x)
            Y.append(numComments)
            dates.append(str(d))
            x+=1
            
   FILE=open("postsComments.csv",'w')
   FILE.write("dates,comments\n")
   for x in X:
      FILE.write(str(dates[x])+","+str(Y[x])+"\n")
      print str(X[x])+","+str(Y[x])
   FILE.close()


      #   year=d.year
         
      #   if "2013" in str(year):
            
      #      if p in postsWithComments:
      #         print "Found Post!"
      #         print len(postsWithComments[p])

   #for p in postsWithComments:
      #print p
   #   if p in datesPostIds:
   #      print str(p)+","+str(datesPostIds[p])

def getTypeContentPost():
   dates = pickle.load(open("postsDates.p", "rb"))

   

   typeContentPerYear={}
   typeContentPerYearUrl={}
   for d in dates:
      year=d.year
      #print year
      typeContentPerYear.setdefault(year,{})
      tipoPosts=dates[d]
      for tipo in tipoPosts:
         #print t
         tLower=tipo.lower()
         if isMedia(tLower):
            tipoFinal="Media"
            #typeContentPerYear[year].setdefault(tipoFinal,0)
            #typeContentPerYear[year][tipoFinal]+=1
         else:
            tipoFinal="Text"
         typeContentPerYear[year].setdefault(tipoFinal,0)
         typeContentPerYear[year][tipoFinal]+=len(tipoPosts[tipo])

   totalYear={}
   totalTodosYears=0
   for year in typeContentPerYear:
      print year

      tipos=typeContentPerYear[year]
      #print len(tipos)
      totalContent=0
      for t in tipos:
         totalTipo=tipos[t]
         totalContent+=totalTipo
         #print t+","+str(totalTipo)
      totalYear[year]=totalContent
      totalTodosYears+=totalContent
      for t in tipos:
         totalTipo=tipos[t]
         percentageTipo=getPercentage(totalContent,totalTipo)
         
         print t+","+str(percentageTipo)
      print

   for y in totalYear:
      #print str(y)+","+str(totalYear[y])
      percentageTipo=getPercentage(totalTodosYears,totalYear[y])
      print str(y)+","+str(percentageTipo)+"/%"




         #percentageTipo=getPercentage(totalPosts, numPostsVideo)
   #print totalContent









      #for t in tipoPosts:
       #  tiposTotales.setdefault(t,0)
        # tiposTotalesYear[year].setdefault(t,0)
        # tiposTotalesYear[year][t]+=len(tipoPosts[t])

         #tiposTotales[t]+=len(tipoPosts[t])
         #tLower=t.lower()
         #foundItsMedia=False
         #for keyword in videoKeywords:
          #  if keyword in tLower:
               #print "Found:"+t
           #    numPostsVideo+=len(tipoPosts[t])
            #   totalPosts+=len(tipoPosts[t])
             #  foundItsMedia=True
              # links=tipoPosts[t]
               #for l in links:
                #  urlsFinal.setdefault(l,0)
                 # urlsFinal[l]+=1


   

def getPercentageFotosYears():
   getTypeContentPost()

   #dates = pickle.load(open("postsDates.p", "rb"))

  # for d in dates:
   #   year=d.year
      



def getEarliestLatestDate():
   dates = pickle.load(open("postsDates.p", "rb"))
   sorted_dates = sorted(dates.items(), key=operator.itemgetter(0),reverse=True)
   i=0
   for d,v in sorted_dates:
      if i==0:
         first=d
      i+=1
         #print d
   last=d
   print first
   print last
      #2012-11-07 22:00:53

def checkDatesPosts():
   datesPostIds=pickle.load(open("datesPostIds.p", "rb"))
   FILE=open("trash.txt",'w')
   for d in datesPostIds:
      print d
      FILE.write(str(d)+"\n")
   FILE.close()

def testPosts():
   posts=pickle.load(open("postsDates.p", "rb"))
   for pID in posts:
      print pID
      print posts[pID]

def participationRatePerYear():

   postsWithComments = pickle.load(open("postsComments.p", "rb"))
   datesPostIds = pickle.load(open("datesPostIDs.p", "rb"))
   sorted_dates = sorted(datesPostIds.items(), key=operator.itemgetter(0),reverse=True)
   participationRate={}
   daysOrdered=[]
   dailyNumComments={}
   dailyNumPosts={}
   for date,postsDay in sorted_dates:
      print date
      day=str(date).split()[0]
      daysOrdered.append(day)
      
      dailyNumComments.setdefault(day,0)
      dailyNumPosts.setdefault(day,0)
      
      numPosts=len(postsDay)
      dailyNumPosts[day]+=numPosts

      for idPost in postsDay:
         if idPost in postsWithComments:
            print "found comments!"
            numComments=len(postsWithComments[idPost])
            dailyNumComments[day]+=numComments

   FILE=open("commentsBronco.csv","w")
   FILE.write("day,pRate\n")
   for d in daysOrdered:
      print d
      participationRate=float(float(dailyNumComments[d])/float(dailyNumPosts[d]))
      print str(d)+","+str(participationRate)
      FILE.write(str(d)+","+str(participationRate)+"\n")
   FILE.close()
   pickle.dump(dailyNumComments,open("dailyNumComments.p", "wb"))
   pickle.dump(dailyNumPosts,open("dailyNumPosts.p", "wb"))

   #print "all we are saying :)"
   #posts.setdefault(idPost,{})
   #posts[idPost][idComment]={}
   #posts[idPost][idComment]["user"]=user
   #posts[idPost][idComment]["time"]=time
   #posts[idPost][idComment]["message"]=message

   #datesPostIds[date][idPost]={}
   #datesPostIds[date][idPost]["tipoPost"]=tipoPost
   #datesPostIds[date][idPost]["url"]=url
   #EdatesPostIds[date][idPost]["texto"]=texto


def getDatesPostsFinal():
   #pickle.dump(datesPostIds, open("datesPostIds.p", "wb"))
   postsWithComments = pickle.load(open("postsComments.p", "rb"))
   #datesPostIds = pickle.load(open("postsDates.p", "rb"))
   datesPostIds = pickle.load(open("datesPostIDs.p", "rb"))
   #pickle.dump(datesPostIDs,open("datesPostIDs.p", "wb"))
   for date in datesPostIds:
      dateString=str(date)
      if "2012" in dateString:
         posts2012=datesPostIds[date]
         for pID in posts2012:
            print pID
            if pID in postsWithComments:
               print pID 
            #print pID
            #   print "found!"+dateString
         break

      #print str(date)
   #datesPostIds[date][idPost]={}
   #datesPostIds[date][idPost]["tipoPost"]=tipoPost
   #datesPostIds[date][idPost]["url"]=url
   #EdatesPostIds[date][idPost]["texto"]=texto

def getCommentsPerYear():
   yearUserComments = pickle.load(open("yearUserComments.p", "rb"))
   commentsYear={}
   for year in yearUserComments:
      print year
      usuarios=yearUserComments[year]
      for u in usuarios:
         numComments=usuarios[u]
         print "Num Comen:"+str(numComments)+","+str(year)
         commentsYear.setdefault(year,0)
         commentsYear[year]+=numComments
   pickle.dump(commentsYear, open("commentsYear.p", "wb"))

def getPercentageBronco(usuariosYear,userID,year):
   userIDs = pickle.load(open("userIDs.p", "rb"))
   commentsYear = pickle.load(open("commentsYear.p", "rb"))
   numCommentsYear=commentsYear[year]
   if userID in usuariosYear:
      numCommentsUserYear=usuariosYear[userID]
      numCommentsUserYear=numCommentsUserYear*100
      numCommentsUserYear=float(float(numCommentsUserYear)/float(numCommentsYear))
      print numCommentsUserYear
      return numCommentsUserYear
   else:
      return 0



def participationRateIndividual():
   yearComments = pickle.load(open("yearComments.p", "rb"))
   yearPosts = pickle.load(open("yearPosts.p", "rb"))
   yearUserComments = pickle.load(open("yearUserComments.p", "rb"))
   keyBronco=1L
   FILE=open("participationRateBronco.csv",'w')
   print
   print "START"
   for year in yearPosts:
      #print year
      comentariosUsuariosYear=yearUserComments[year]
      if keyBronco in comentariosUsuariosYear:
         comentariosIndividualesYear=comentariosUsuariosYear[keyBronco]
         rate=float(float(comentariosIndividualesYear)/float(yearPosts[year]))
         
      else:
         comentariosIndividualesYear=0
         rate=0

      #print comentariosIndividualesYear
      FILE.write(str(year)+","+str(rate)+"\n")
      print str(year)+","+str(rate)
   FILE.close()



   #numCommentsUserYear=usuariosYear[userID]

def getYearComments_Posts():
   dailyNumComments = pickle.load(open("dailyNumComments.p", "rb"))
   dailyNumPosts = pickle.load(open("dailyNumPosts.p", "rb"))
   yearComments={}
   yearPosts={}
   for date in dailyNumComments:
      print date
      year=date.split("-")[0]
      print year
      print (dailyNumComments[date])
      yearComments.setdefault(year,0)
      yearComments[year]+=dailyNumComments[date]

   for date in dailyNumPosts:
      print date
      year=date.split("-")[0]
      print year
      print (dailyNumPosts[date])
      yearPosts.setdefault(year,0)
      yearPosts[year]+=dailyNumPosts[date]
      #2013-08-25

   pickle.dump(yearComments,open("yearComments.p", "wb"))
   pickle.dump(yearPosts,open("yearPosts.p", "wb"))


#def understandTopCommenters():

def understandTopCommenters():
   topUsers={}
   topUsersFinal={}
   yearUserComments = pickle.load(open("yearUserComments.p", "rb"))
   yearPosts = pickle.load(open("yearPosts.p", "rb"))
   #pickle.dump(yearPosts,open("yearPosts.p", "wb"))

   for year in yearUserComments:
      usuarios=yearUserComments[year]
      for u in usuarios:
         #print str(u)+","+str(usuarios[u])
         topUsers.setdefault(u,0)
         topUsers[u]+=usuarios[u]
   sorted_topUsers = sorted(topUsers.items(), key=operator.itemgetter(1),reverse=True)
   i=0
   print "TOP"
   for u,v in sorted_topUsers:
      if i<5:
         print str(u)+","+str(v)
         topUsersFinal.setdefault(u,v)
      else:
         break
      i+=1
   print 
   for u in topUsersFinal:
      v=topUsersFinal[u]
      print str(u)+","+str(v)
      FILE=open("participationRate_"+str(u)+".csv",'w')
      for y in yearUserComments:
         postsAno=yearPosts[y]
         v=float(float(v)/float(postsAno))
         FILE.write(str(y)+","+str(v)+"\n")
         print y
         print postsAno
         print


def buildHistogramCommentsBronco(numCommentsBroncoPost):
   histogramComments={}
   for post in numCommentsBroncoPost:
      numComments=numCommentsBroncoPost[post]
      histogramComments.setdefault(numComments,0)
      histogramComments[numComments]+=1
   return histogramComments

def getHistogramRepliesBronco():
   postsWithComments = pickle.load(open("postsComments.p", "rb"))
   datesPostIds = pickle.load(open("datesPostIDs.p", "rb"))
   userIDs = pickle.load(open("userIDs.p", "rb"))
   idBronco=1L
   numCommentsBroncoPost={}

   for date in datesPostIds:
      print date
      #print date
      posts=datesPostIds[date]
      for p in posts:
         if p in postsWithComments:
            comments=postsWithComments[p]
            for cID in comments:
               #print cID
               user=comments[cID]
               userID=user["user"]
               if idBronco==userID:
                  #print idBronco
                  numCommentsBroncoPost.setdefault(p,0)
                  numCommentsBroncoPost[p]+=1
   histogramComments=buildHistogramCommentsBronco(numCommentsBroncoPost)
   sorted_histogramComments = sorted(histogramComments.items(), key=operator.itemgetter(0),reverse=True)
   FILE=open("histogramBroncoComments.csv",'w')
   FILE.write("Num_Replies_Bronco,Occurances\n")
   for h,v in sorted_histogramComments:
      print str(h)+","+str(v)
      FILE.write(str(h)+","+str(v)+"\n")
   FILE.close()

              



def understandTopCommenters2():
   #pickle.dump(yearUserComments, open("yearUserComments.p", "wb"))
   #(1L, '259659740767219', 'Jaime Rodriguez Calderon', None, None, None, None)
   #pickle.dump(userIDs, open("userIDs.p", "wb"))
   #pickle.dump(userFBIDs, open("userFBIDs.p", "wb"))
   yearUserComments = pickle.load(open("yearUserComments.p", "rb"))
   userIDs = pickle.load(open("userIDs.p", "rb"))
   userFBIDs = pickle.load(open("userFBIDs.p", "rb"))
   commentsYear = pickle.load(open("commentsYear.p", "rb"))
   #IDsTopCommentersYear={}



   yearCommentsPersona={}
   yearCommentsIndividuo={}
   #pickle.dump(commentsYear, open("commentsYear[.p", "wb"))
   for year in yearUserComments:
      print year
      usuarios=yearUserComments[year]
      userID=1L
      numCommentsUserYear=getPercentageBronco(usuarios,userID,year)
      yearCommentsPersona[year]=numCommentsUserYear

      #yearCommentsIndividuo
   sorted_yearCommentsPersona = sorted(yearCommentsPersona.items(), key=operator.itemgetter(0),reverse=True)
   FILE=open("PorcentajeBroncoContestacion.csv",'w')
   for y,v in sorted_yearCommentsPersona:
      print str(y)+","+str(v)
      FILE.write(str(y)+","+str(v)+"\n")
   FILE.close()
   participationRateIndividual()


   #getYearComments_Posts()
      #print len(usuarios)
      #sorted_usuarios = sorted(usuarios.items(), key=operator.itemgetter(1),reverse=True)
      #i=0
      #print "Top Commenters:"+str(year)
      #for u,v in sorted_usuarios:
      #   if i<10:
            
      #      if u in userIDs:
      #         print "FOUND!"+str(userIDs[u])+","+str(v)
      #   else:
      #      break
      #   i+=1
      #keyBronco=1L
      #if keyBronco in usuarios:
      #   print "Respuestas Bronco:"+str(usuarios[1L])
      #else:
      #   print "Respuestas Bronco:0"

   #getCommentsPerYear()


   #print userIDs[1L]
   #(1L, '259659740767219', 'Jaime Rodriguez Calderon', None, None, None, None)
   #for u in userIDs:
   #   print "ERES:"+str(u)
def getRepliesComments():

   postsWithComments = pickle.load(open("postsComments.p", "rb"))
   datesPostIds = pickle.load(open("datesPostIDs.p", "rb"))
   yearUserComments={}
   yearUserPosts={}
   for date in datesPostIds:
      #2013-08-12 19:11:50
      dateString=str(date).split()[0]
      year=dateString.split("-")[0]
      postsIDs=datesPostIds[date]
      for pID in postsIDs:
         if pID in postsWithComments:
            comments=postsWithComments[pID]
            for cID in comments:
               usuario=comments[cID]["user"]
               print usuario
               yearUserPosts.setdefault(year,{})
               yearUserPosts[year].setdefault(usuario,{})
               yearUserPosts[year][usuario].setdefault(pID,0)
               yearUserPosts[year][usuario][pID]+=1

               yearUserComments.setdefault(year,{})
               yearUserComments[year].setdefault(usuario,0)
               yearUserComments[year][usuario]+=1

   for year in yearUserComments:
      print year
      usuarios=yearUserComments[year]
      #print len(usuarios)
      sorted_usuarios = sorted(usuarios.items(), key=operator.itemgetter(1),reverse=True)
      i=0
      print "Top Commenters:"+str(year)
      for u,v in sorted_usuarios:
         if i<10:
            print str(u)+","+str(usuarios[u])
         else:
            break
         i+=1
      #print len(sorted_usuarios)
      print
   pickle.dump(yearUserComments, open("yearUserComments.p", "wb"))

      #sorted_usuarios = sorted(usuarios.items(), key=operator.itemgetter(1),reverse=True)

      #for u,v in sorted_usuarios:
      #   str(u)+","+str(v)


      #if "2013" in dateString:
      #   postsIDs=datesPostIds[date]
      #   for pID in postsIDs:
      #      if pID in postsWithComments:
      #         print "Found in 2013:"+str(pID)
      #         print year
      #dateString=str(date)
      #if "2013" in dateString:
      #   print date

      #posts.setdefault(idPost,{})
      #posts[idPost][idComment]={}
      #posts[idPost][idComment]["user"]=user
      #posts[idPost][idComment]["time"]=time
      #posts[idPost][idComment]["message"]=message



   #postsWithComments = pickle.load(open("postsComments.p", "rb"))
   #for idPost in postsWithComments:
   #   comments=postsWithComments[idPost]
   #   fechas={}
   #   for idComment in comments:
   #      date=comments[idComment]["time"]
   #      fechas[date]=0
   #sorted_fechas = sorted(fechas.items(), key=operator.itemgetter(0),reverse=True)
   #for d,v in sorted_fechas:
   #   print d
      #dateString=str(d)
      #if "2014" in dateString:
      #   print "found!"+dateString
      #   break
      #break




def getRepliesComments2():
   postsWithComments = pickle.load(open("postsComments.p", "rb"))

   #posts[idPost][idComment]={}
   #posts[idPost][idComment]["user"]=user
   #posts[idPost][idComment]["time"]=time
   #posts[idPost][idComment]["message"]=message
   usersComments={}
   postUserC={}
   for idPost in postsWithComments:
      comments=postsWithComments[idPost]
      #postUserC[]
      for idComment in comments:
         #print comments[idComment]["user"]
         username=comments[idComment]["user"]
         usersComments.setdefault(username,0)
         usersComments[username]+=1
         postUserC.setdefault(username,{})
         postUserC[username].setdefault(idPost,0)
         postUserC[username][idPost]+=1

   arrayUserComments={}
   for u in postUserC:
      #print u
      arrayUserComments.setdefault(u,[])
      for idPost in postUserC[u]:
         valor= postUserC[u][idPost]
         arrayUserComments[u].append(valor)

   for u in arrayUserComments:
      if str(u)=="2534":
         print u
         arrayU=arrayUserComments[u]
         arrayU.sort()
         median=len(arrayU)/2
         median=arrayU[median]
         print "Median:"+str(median)
         for c in arrayU:
            print c
            print c

      #
      #2534,1222,1.24948875256

      #257,527,0.538854805726

      #7541,467,0.477505112474

      #4498,446,0.456032719836

      #37775,409,0.418200408998
      #for v in arrayU:
      #   print u



         #break
         #print idComment
      #print c
      #print c["user"]
      #print 
      #break
   #sorted_usersComments = sorted(usersComments.items(), key=operator.itemgetter(1),reverse=True)
   #i=0
   #for u,v in sorted_usersComments:
    #  if i<5:
         
     #    average=float(float(v)/float(len(postsWithComments)))
      #   print str(u)+","+str(v)+","+str(average)
       #  print
      #else:
      #   break
      #i+=1
   #print "Num Posts:"+str(len(postsWithComments))

def getCommentsOverTimeArrays():
   postsTexts=pickle.load(open("postsDates.p", "rb"))
   comments = pickle.load(open("postsComments.p", "rb"))
   datesPostIds=pickle.load(open("datesPostIds.p", "rb"))
   sorted_dates = sorted(datesPostIds.items(), key=operator.itemgetter(0),reverse=True)
   daysOrdered=[]
   dailyNumComments={}
   dailyNumPosts={}
   topComments={}
   for d,dictDates in sorted_dates:
      day=str(d).split()[0]
      daysOrdered.append(day)
      #datesDict.setdefault(day,[])
      #datesDict[day].append(d)
      #print str(d)
      dailyNumComments.setdefault(day,[])
      dailyNumPosts.setdefault(day,0)
      
      numPosts=len(dictDates)
      dailyNumPosts[day]+=numPosts
      for idPost in dictDates:
         if idPost in comments:
            print "found comments!"
            print len(comments[idPost])
            #dailyMedianNumComments[day].append(len(comments[idPost]))
            dailyNumComments[day].append(len(comments[idPost]))
            numComments=len(comments[idPost])
            topComments.setdefault(numComments,{})
            topComments[numComments].setdefault(d,{})
            topComments[numComments][d][idPost]=day
   x=[]
   y=[]
   z=[]
   zCounter=0
   #dailyMedianNumComments.sort()

   for d in daysOrdered:
      print d
      numCommentsPosts=dailyNumComments[d]
      numCommentsPosts.sort()
      print "Length Posts:"+str(dailyNumPosts[d])
      #median=len(numCommentsPosts)/2
      #median=numCommentsPosts[median]
      #for c in numCommentsPosts:
      #   print c
      #print "Median:"+str(median)
      for  c in numCommentsPosts:
         x.append(d)
         y.append(c)
         z.append(zCounter)
         zCounter+=1
   FILE=open("commentsBronco.csv","w")
   FILE.write("date,comment\n")
   for zCounter in z:
      print zCounter
      print str(x[zCounter])+","+str(y[zCounter])
      FILE.write(str(x[zCounter])+","+str(y[zCounter])+"\n")
   FILE.close()
   sorted_topComments = sorted(topComments.items(), key=operator.itemgetter(0),reverse=True)
   i=0
   for numComments, dictComments in sorted_topComments:
      if i<10:
         print numComments
         #topComments[numComments][d][idPost]=day
         for postID in dictComments:
            print str(postID)+","+str(dictComments[postID])
            text=postsTexts[postID]
            print "Texto:"+str(text)
         print
         print

      else:
         break
      i+=1
   #6702
   #2015-07-29 19:22:27,{781L: '2015-07-29'}
   #topComments[numComments][idPost]=day



def getCommentsOverTime():
   #dates = pickle.load(open("postsDates.p", "rb"))
   comments = pickle.load(open("postsComments.p", "rb"))
   datesPostIds=pickle.load(open("datesPostIds.p", "rb"))
   sorted_dates = sorted(datesPostIds.items(), key=operator.itemgetter(0),reverse=True)
   #tipoPostsCount={}
   
   dailyNumComments={}
   dailyMedianNumComments={}
   dailyNumPosts={}
   dailyReplyRate={}
   datesDict={}
   daysOrdered=[]
   for d,dictDates in sorted_dates:
      
      day=str(d).split()[0]
      daysOrdered.append(day)
      datesDict.setdefault(day,[])
      datesDict[day].append(d)
      print str(d)
      dailyNumComments.setdefault(day,0)
      dailyNumPosts.setdefault(day,0)
      dailyMedianNumComments.setdefault(day,[])
      numPosts=len(dictDates)
      dailyNumPosts[day]+=numPosts

      for idPost in dictDates:
         if idPost in comments:
            print "found comments!"
            print len(comments[idPost])
            dailyMedianNumComments[day].append(len(comments[idPost]))
            dailyNumComments[day]+=len(comments[idPost])

   x=[]
   y=[]
   z=[]
   zCounter=0
   #dailyMedianNumComments.sort()
   for d in daysOrdered:
      print d
      numCommentsPosts=dailyMedianNumComments[d]
      numCommentsPosts.sort()
      print "Length Posts:"+str(dailyNumPosts[d])
      median=len(numCommentsPosts)/2
      median=numCommentsPosts[median]
      for c in numCommentsPosts:
         print c
      print "Median:"+str(median)
      
      x.append(d)
      y.append(median)
      z.append(zCounter)
      zCounter+=1
   FILE=open("commentsBronco.csv","w")
   FILE.write("date,comment\n")
   for zCounter in z:
      print zCounter
      print str(x[zCounter])+","+str(y[zCounter])
      FILE.write(str(x[zCounter])+","+str(y[zCounter])+"\n")
   FILE.close()


   #for d in dailyNumPosts:
   #   print str(d)+","+str(dailyNumPosts[d])+","+str(dailyNumComments[d])
   #   if dailyNumComments[d]==0:
   #      rate=0
   #   else:
   #      rate=float(float(dailyNumPosts[d])/float(dailyNumComments[d]))
   #   print rate
   #   dailyReplyRate[d]=rate

  # for d in dailyReplyRate:
   #   print str(d)+","+str(dailyReplyRate[d])



         #print idPost

         #keysPost=dictDates[idPost]

         #for k in keysPost:
         #   print k
            #tipoPost
            #url
            #texto
      #+","+str(v)
   #for d in 

   # pickle.dump(datesPostIds, open("datesPostIds.p", "wb"))


def getUsers():
   #(1L, '259659740767219', 'Jaime Rodriguez Calderon', None, None, None, None)
   userIDs={}
   userFBIDs={}
   db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="nathan",  # your password
                     db="politics")        # name of the data base
   cur = db.cursor()
   # Use all the SQL you like
   cur.execute("SELECT * FROM user;")
   print "got users!"
   posts={}
   for row in cur.fetchall():
      #(1L, '259659740767219', 'Jaime Rodriguez Calderon', None, None, None, None)
      userID=row[0]
      FBUserID=row[1]
      name=row[2]
      #print row
      userIDs[userID]=name
      userFBIDs[FBUserID]=name
      #break
   pickle.dump(userIDs, open("userIDs.p", "wb"))
   pickle.dump(userFBIDs, open("userFBIDs.p", "wb"))


def getCommentsPost():
   db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="nathan",  # your password
                     db="politics")        # name of the data base
   cur = db.cursor()
   # Use all the SQL you like
   cur.execute("SELECT * FROM comment;")
   print "got comments!"
   posts={}
   for row in cur.fetchall():
      #print row
      idComment=row[0]
      idPost=row[1]
      fbLink=row[2]
      user=row[3]
      message=row[4]
      time=row[6]
      likeCount=row[7]
      userLike=row[8]
      posts.setdefault(idPost,{})
      posts[idPost][idComment]={}
      posts[idPost][idComment]["user"]=user
      posts[idPost][idComment]["time"]=time
      posts[idPost][idComment]["message"]=message
      #print "IDComment:"+str(idComment)
      #print "IDPost:"+str(idPost)
      #print "user:"+str(user)
      #print "message:"+str(message)
      #print "time"+str(time)
      #print "likeCount:"+str(likeCount)
      #print "UserlikeCount:"+str(userLike)
      #print fbLink
   pickle.dump(posts, open("postsComments.p", "wb"))
      #print "IDComment:"+str(idComment)
      #break


def getPostIDs():
   db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="nathan",  # your password
                     db="politics")        # name of the data base
   cur = db.cursor()
   # Use all the SQL you like
   cur.execute("SELECT * FROM post;")
   # print all the first cell of all the rows
   dates={}
   datesPostIds={}
   numPosts=0

   for row in cur.fetchall():
      #print row
      idPost=row[0]
      date=row[3]
      user=row[5]
      #print idPost
      if not date==None:
         tipoPost=row[11]
         texto=row[12]
         url=row[10]

         if not tipoPost==None:
            dates.setdefault(date,{})
            datesPostIds.setdefault(date,{})
            datesPostIds[date][idPost]={}
            datesPostIds[date][idPost]["tipoPost"]=tipoPost
            datesPostIds[date][idPost]["url"]=url
            datesPostIds[date][idPost]["texto"]=texto


            dates[date].setdefault(tipoPost,{})
            dates[date][tipoPost][url]=texto
            #print tipoPost
            #print texto
            #print url
            numPosts+=1
      #break
   pickle.dump(datesPostIds, open("datesPostIds.p", "wb"))
   print len(datesPostIds)

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
   datesPostIDs={}
   numPosts=0
   for row in cur.fetchall():
      #print row
      idPost=row[0]
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

            datesPostIDs.setdefault(date,{})
            datesPostIDs[date].setdefault(idPost,{})
            datesPostIDs[date][idPost]=texto


            #print tipoPost
            #print texto
            #print url
            numPosts+=1
            #print
         
   print numPosts
   pickle.dump(dates, open("postsDates.p", "wb"))
   pickle.dump(datesPostIDs,open("datesPostIDs.p", "wb"))

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

testComments()
#getHistogramRepliesBronco()
#testComments()
#correctCSVComments()
#understandTopCommenters()
#participationRatePerYear()

#getUsers()
#getRepliesComments()

#participationRatePerYear()
#getCommentsPost()
#getRepliesComments()

#getDatesPost()
#getDatesPost()
#getDatesPostsFinal()

#testPosts()
#getCommentsOverTimeArrays()
#checkDatesPosts()
#getPostIDs()
#getCommentsPost()
#getCommentsOverTime()
#getPostIDs()
#getCommentsOverTime()
#getDatesPost()      
#getCommentsPost()
#getTypeContentPost()
#getDatesPost()
#getNumPhotosVideoShared()
#getEarliestLatestDate()
#getPercentageFotosYears()
#getNumPhotosVideoShared()

#getPostDataFrom()
#getDatesPost()
#getNumPhotosVideoShared()

#sorted_dates = sorted(dates.items(), key=operator.itemgetter(0),reverse=True)
#for d,v in sorted_dates:
#  print d

    #break
