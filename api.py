import os,sys,time,libvirt
from log import *

## Connect to server
try:
	conn = libvirt.open('qemu:///system')
	logStatus("Connected to QEMU")
except:
	logError("Could not connect to QEMU")

## VMs

def listVMs():
	for i in conn.listAllDomains():
            print(i.name())

def returnVMs():
	domainList = []
	for i in conn.listAllDomains():
		domainList.append(i.name())
	return domainList

def startAllVMs():
	for domain in conn.listAllDomains():
			vm = str(domain.name())
			startVM(vm)

def stopAllVMs():
	for domain in conn.listAllDomains():
			vm = str(domain.name())
			stopVM(vm)

def startVM(vm_name):
	try:
		conn.lookupByName(vm_name).create()
		logStatus("Starting "+vm_name)
	except:
		logError("Error starting "+vm_name)

def stopVM(vm_name):
	try:
		conn.lookupByName(vm_name).destroy()
		logStatus("Stopping "+vm_name)
	except:
		logError("Error stopping "+vm_name)

def createVM(vm_name):
	f = open(os.path.dirname(os.path.realpath(__file__))+"/images/"+vm_name+".xml")
	conn.defineXML(f.read())
	conn.lookupByName(vm_name).create()

def listNets():
	for nets in conn.listAllNetworks():
		print(nets.name())

def returnNets():
	netList = []
	for nets in conn.listAllNetworks():
		netList.append(str(nets.name()))
	return netList

## Images

def listImages():
	for file in os.listdir("./images/"):
                        if file.endswith(".xml"):
                                print(file)


if __name__ == "__main__":
        conn = libvirt.open('qemu:///system')

