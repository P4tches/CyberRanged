import os,sys,time
from api import *
from db import *

vm_name = 0
env_name = 0
storageMedia = 0
net_name = 0

## Generate VM xml from Database
def main():
	global vm_name
	global env_name
	clearScreen()
	print("Welcome to XMLgen")
	print()
	print("VM name?:")
	vm_name = input("> ")
	## list environments from db
	print(listAllEnv())
	print("Select environment:")
	env_name = input("(%s)> " % vm_name)
	mediaType()
	network()
	printAll()

def mediaType():
	global storageMedia
	print("Media type?")
	print("1) ISO")
	print("2) VMDK")
	option = input("(%s)> " % vm_name)
	if option == "1":
		storageMedia="cdrom"
	elif option == "2":
		storageMedia="vmdk"
	else:
		print("ERROR: unknown selection")
		mediaType()

def network():
	global net_name
	## print networks in environment
	print("Which network?") # list by numbers instead of string input
	count = 1
	nets = listNets(env_name)
	for i in nets:
		print(i)
	#print(listNets("env7"))
	option = input("(%s)> " % vm_name)
	net_name = option

def printAll():
	print("VM: "+str(vm_name))
	print("Env: "+str(env_name))
	print("Storage: "+str(storageMedia))
	print("Net: "+str(net_name))

def clearScreen():
	os.system("clear")

if __name__ == "__main__":
	main()
