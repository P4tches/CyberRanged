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
	## print networks in environment
	print("Which network?") # list by numbers instead of string input
	option = input("(%s)> " % vm_name)

def printAll():
	print("VM: "+vm_name)
	print("Env: "+env_name)
	print("Storage: "+storageMedia)

def clearScreen():
	os.system("clear")

if __name__ == "__main__":
	main()
