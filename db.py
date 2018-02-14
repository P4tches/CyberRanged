import sqlite3
from datetime import datetime, date
conn = sqlite3.connect('env.db')
c = conn.cursor()

#def main():
#	print("Hello DB!")
#	createEnv("env9")
#	addEnvVM("env9","Kali_07","env_07")
	#delEnvVM("env9","Kali_02")
	#deleteEnv("env4")
#	listEnv("env9")
#	listAllEnv()
#	conn.close()

def createEnv(env_name):
	try:
		c.execute('''CREATE TABLE %s (image_name text,network_name text,vm_timestamp)''' % env_name)
		conn.commit()
	except:
		print("ERROR:Could not create environment")

def deleteEnv(env_name):
	try:
		c.execute('''DROP TABLE %s''' % env_name)
	except:
		print("ERROR: Could not delete environment")

def addEnvVM(env_name,vm_name,vm_net):
	vm_create_time=datetime.now()
	try:
		c.execute(str('''INSERT INTO {} VALUES ('{}','{}','{}')''').format(env_name,vm_name,vm_net,vm_create_time))
		conn.commit()
	except:
		print("ERROR: Could not add VM to environment")

def delEnvVM(env_name,vm_name):
	try:
		c.execute(str('''DELETE FROM {} WHERE image_name='{}';''').format(env_name,vm_name))
		conn.commit()
	except:
		print("ERROR: Could not delete VM to environment")

def listEnv(env_name):
	try:
		c.execute("SELECT * FROM %s" % env_name)
		print(c.fetchall())
	except:
		print("ERROR: Could not list environment")

def listAllEnv():
	try:
		#c.execute(".tables")
		c.execute("SELECT name FROM sqlite_master WHERE type='table';")
		print(c.fetchall())
	except:
		print("ERROR: Could not list environments")

def listNets(env_name):
	try:
		c.execute("SELECT network_name FROM %s" % env_name)
		return c.fetchall()
	except:
		print("ERROR: Could not list networks")

def selectLine(table,line):
	## 0 == first line of output
	print("test")
	c.execute(str("SELECT * FROM {} LIMIT 1 OFFSET {}").format(table,line))
	print(c.fetchall())
#if __name__ == "__main__":
#	conn = sqlite3.connect('env.db')
#	c = conn.cursor()
#	print(listAllEnv())
#	main()
