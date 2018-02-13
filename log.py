import os,datetime
dir = os.getcwd()
errorLog = dir+'/logs/status.log'
statusLog = dir+'/logs/status.log'



def logError(errorMessage):
	f = open(errorLog,'a')
	f.write("\n"+str(datetime.datetime.now())+" [*] "+errorMessage)
	f.close()

def logStatus(statusMessage):
	f = open(statusLog,'a')
	f.write("\n"+str(datetime.datetime.now())+" [*] "+statusMessage)
	f.close()
