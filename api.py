import os,sys,time,libvirt


#def main():
	#listVMs()
	#stopVM("Kali_01")
	#listImages()

## Connect to server
try:
	conn = libvirt.open('qemu:///system')
except:
	print("Could not connect to QEMU")

## VMs

def listVMs():
	for i in conn.listAllDomains():
                        print(i.name())

def startAllVMs():
	for domain in conn.listAllDomains():
			vm = str(domain.name())
			print("Starting "+vm)
			try:
				domain.create()
			except:
				print("Error starting "+vm)

def stopAllVMs():
	for domain in conn.listAllDomains():
			vm = str(domain.name())
			print("Stopping "+vm)
			try:
				domain.destroy()
			except:
				print("Error stopping "+vm)

def startVM(vm_name):
	try:
		conn.lookupByName(vm_name).create()
	except:
		print("Error starting "+vm_name)

def stopVM(vm_name):
	try:
		conn.lookupByName(vm_name).destroy()
	except:
		print("Error stopping "+vm_name)

def createVM(vm_name):
	f = open(os.path.dirname(os.path.realpath(__file__))+"/images/"+vm_name+".xml")
	conn.defineXML(f.read())
	conn.lookupByName(vm_name).create()

def listNets():
	for nets in conn.listAllNetworks():
		print(nets.name())


## Images

def listImages():
	for file in os.listdir("./images/"):
                        if file.endswith(".xml"):
                                print(file)


if __name__ == "__main__":
        conn = libvirt.open('qemu:///system')
#        main()
