# Tool - 1 Findip:
from scapy.all import *


def IsAlive(Address):
	Packet = ARP(pdst=Address)
	Brod = Ether(dst="ff:ff:ff:ff:ff:ff")
	Concat = Brod / Packet
	Rply = srp(Concat,timeout=1)[0]
	print(" [ * ] Found Ip Address :")
	Counter = 0
	for Ack in Rply:
		Counter+=1
		print(f"[ {Counter} ] ",str(Ack).split("|")[3].split(" ")[9].split("=")[1])
Ip = input(str(" [ * ] Enter the  Ip Address:"))
IsAlive(Ip)










