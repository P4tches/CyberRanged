import os,sys,time,libvirt
from api import *
from log import *

def main():
	logStatus("main.py started")
	clearScreen()
	print("Welcome to CyberRange Alpha")
	print()
	print("Options:")
	print("1) Install Environment")
	print("2) Manage Environment")
	print("3) Manage Images")
	print()
	option = input("(main)> ")
	print()
	if option == "1":
		install()
	elif option == "2":
		manage_environment()
	elif option == "3":
		manage_images()
	elif option == "4": #api test option
		listVMs()
	elif option == "back" or option == "exit":
		print("bye bye!")
		sys.exit(0)
	else:
		print("Input ERROR")
		time.sleep(1)
	clearScreen()


def install():
	print("CyberRange Install...done")
	time.sleep(1)
	main()

def manage_environment():
	print("Environment Management")
	print("1) List Hosts")
	print("2) Start Environment")
	print("3) Stop Environment")
	print("4) Import Environment")
	print("5) Destroy Environment") #implement safe-guard
	print("6) Start VM")
	print("7) Stop VM")
	option = input("(env)> ")
	if option == "1":
		print("===========")
		listVMs()
		print("===========")
		print()
	elif option == "2":
		startAllVMs()
	elif option == "3":
		stopAllVMs()
	elif option == "4":
		print("Importing env...Done")
	elif option == "5":
		print("Destroying env...Done")
	elif option == "6":
		name = input("VM Name:")
		startVM(name)
	elif option == "7":
		name = input("VM Name:")
		stopVM(name)
	elif option == "back":
		main()
	time.sleep(1)
	manage_environment()

def manage_images():
	print("Image Management")
	## Location ./images
	print("1) List Images")
	print("2) Import Image")
	print("3) Delete Image")
	print("4) Create VM")
	print("5) Delete VM")
	option = input("(img)> ")
	if option == "1":
		print("===========")
		listImages()
		print("===========")
		print()
	elif option == "2":
		print("Image Import...done")
	elif option == "3":
		print("Image Delete...done")
	elif option == "4":
		name = input("Image Name:")
		createVM(name)
	elif option == "back":
		main()
	else:
		print("Input ERROR")
		time.sleep(1)
	manage_images()

def clearScreen():
	os.system("clear")

def open_libvirt():
	conn = libvirt.open('qemu:///system')

if __name__ == "__main__":
	conn = libvirt.open('qemu:///system')
	main()
