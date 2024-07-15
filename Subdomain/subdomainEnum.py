# SubDomain BruteForce
# ************************
# Author : Mr Whitehat
# Last Created : 11 - 7 - 24
# Updated : 11 - 7 - 24
# ***************************
import os
import requests
import time
import threading
import sys
import socket
import datetime 





class BruteForce:
	def __init__(self):
		self.config = {}
		self.Counter=0
		self.Fileops = self.GetDate().minute
	def ConfigureArgs(self):
		if(len(sys.argv) == 5):
			for Args in sys.argv:
				if "--" in Args:
					conf = Args.replace("--","").strip()
					if conf.lower() == "wordlist":
						if os.path.exists(sys.argv[sys.argv.index(Args)+1]):
							self.config[conf] = sys.argv[sys.argv.index(Args)+1]
						else:
							return False
					else:
						self.config[conf] = sys.argv[sys.argv.index(Args)+1]
			return True
		else:
			return False
	def cls(self):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")

	def LoadWordlist(self):
		Lst = []
		with open(self.config["wordlist"],'r') as File:
			for Line in File.readlines():
				Lst.append(Line.strip())
			File.close()
		return Lst
	def usage(self):
		print(f"\n [ * ] Usage : {sys.argv[0]} --wordlist <file> --domain <domain>")
		print("\n  --wordlist - wordlist file which contains domain List [ default to seclist dns wordlist ]")
		print("\n  --domain - target domain to be Scanned")
	def GetBanner(self,address):
		s = socket.socket()
		s.connect((address,80))
		Ban = s.recv(1024).decode()
		s.close()
		return Ban
	def WriteOps(self,data):
		file = f"Report-{self.Fileops}.txt"
		if os.path.exists(file):
			with open(file,'a') as File:
				File.write(data+"\n")
				File.close()
		else:
			with open(file,'w') as File:
				File.write(data+"\n")
				File.close()
	def RequestPage(self,Sub):
		if self.isComputerOnline():
			Payload = f'{Sub}.{self.config["domain"]}'
			try:
				response = requests.get("http://"+Payload)
				self.WriteOps(f"{response.status_code} - {Payload}")
				print(f"[+] {response.status_code}\t\t\t{Payload} \t\t{socket.gethostbyname(Payload)}")
				self.Counter+=1
			except:
				pass
		
	

	def isComputerOnline(self):
		host = "www.google.com"
		port = 80
		while True:
			s = socket.socket(socket.AF_INET,socket.AF_INET)
			try:
				s.connect((socket.gethostbyname(host),port))
				s.close()
				return True
			except:
				s.close()
	def GetDate(self):
		return datetime.datetime.now()
	def ControllerCode(self):
		self.cls()
		if self.ConfigureArgs():
			Loaded = self.LoadWordlist()
			print("================Info==============================================")
			print("\n[ + ]Wordlist Count: ",len(Loaded))
			print("\n[ + ]Target:",self.config["domain"])
			print("\n[ + ]Ip Address:",socket.gethostbyname(self.config["domain"]))
			now = self.GetDate()
			print("\n[ + ] Time Info :",now)
			# Min = now.minute
			print("="*69)
			print("  statusCode\t\t\tdomain \t\t\tIp")
			print("="*69)
			counter = 0
			for Sub in Loaded:
				t = threading.Thread(target=self.RequestPage,args=(Sub,))
				t.start()
				
			print("[ * ] Found :",self.Counter)
			# now = self.GetDate()
			# Min2 = now.minute

			# print("Time Taken : ",Min2 - Min,"Minutes !")
			print("="*69)
			print("Result : ",os.getcwd()+"\\"+f"Report-{str(self.Fileops)}.txt")
			print("="*69)
		else:
			self.usage()

B = BruteForce()
B.ControllerCode()