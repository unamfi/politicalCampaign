import pickle
from random import randrange, uniform

def secondRun():
	print "Second run!"
	miDict = pickle.load(open("dictTest.p", "rb"))
	print "Original"
	for i in miDict:
		print i
	print 
	print "New Data Added"
	miDict.append(randrange(0, 10))
	miDict.append(randrange(0, 10))
	for i in miDict:
		print i
	pickle.dump(miDict, open("dictTest.p", "wb"))


def firstRun():
	print "1st run!"
	miDict=[]
	print "Original"
	for i in miDict:
		print i
	print 
	print "New Data Added"
	#irand = randrange(0, 10)
	miDict.append(randrange(0, 10))
	miDict.append(randrange(0, 10))
	for i in miDict:
		print i
	pickle.dump(miDict, open("dictTest.p", "wb"))

firstRun()
secondRun()


	#dates = pickle.load(open("postsDates.p", "rb"))
	#pickle.dump(dates, open("postsDates.p", "wb"))