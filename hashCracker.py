import os
import hashlib
import sys
from pyfiglet import print_figlet
import threading
from time import sleep
from colorama import init,Fore

class cracker:
    def __init__(self):
    	self.G = Fore.GREEN
    	self.R = Fore.RED
    	self.Y = Fore.YELLOW
    	self.N = Fore.WHITE
    	self.config = {}
    	self.Found = False
    	self.hashAlgoList = ["sha512","sha256","md5","sha224","sha384","sha1","sha3_224","sha3_256","sha3_512","sha3_384"]
    def usage(self):
    	print(f"usage : {sys.argv[0]} --wordlist <wordlist file> --hash <hash to crack> --type <md5>")
    	print("\n --wordlist - wordlist file to be specified")
    	print("\n --hash    -   hash to be cracked")
    	print('\n --type  - ["sha512","sha256","md5","sha224","sha384","sha1","sha3_224","sha3_256","sha3_512","sha3_384"] any type in list')
    def cls(self):
    	if os.name =="nt":
    	    os.system("cls")
    	    self.config["os"] = "windows"
    	else:
    	    os.system("clear")
    	    self.config["os"] = "linux"
    def configureArgs(self):
    	self.cls()
    	print(self.Y)
    	self.renderBanner("hash cracker")
    	print(self.N)
    	if len(sys.argv) == 7:
    	    print("\n[ + ] Configuring Args ")
    	    sleep(0.5)
    	    for configs in range(len(sys.argv)-1):
    	    	if "--" in sys.argv[configs]:
    	    	    self.config[sys.argv[configs].replace("--","").strip()] = sys.argv[configs+1].strip()
    	
    	    if self.config["type"] in self.hashAlgoList and (os.path.exists(self.config["wordlist"])and os.path.isfile(self.config["wordlist"])):
    	    	print("\n [ + ] Configuration SuccessFull")
    	    	return True
    	    else:
    	    	print("[ ! ] Specified hash Not Supported [ or ]  [ ! ] File Config Error ")
    	    	self.usage()
    	    	
    	    	return False
    	else:
    	    
    	    print("Config Error [!]")
    	    self.usage()
    	    return False
    def renderBanner(self,graph):
    	print_figlet(graph)
  
  
    def loadWordlist(self):
    	with open(self.config["wordlist"],'rb') as F:
    		wordlist = F.readlines()
    		F.close()
    		
    	return wordlist
    	
    def downloadCustomWordlist(self):
    	pass
    def returnhash(self):
    	if self.config["type"] == "sha512":
    	    self.config["type"] = hashlib.sha512
    	elif self.config["type"] == "sha256":
    	    self.config["type"] = hashlib.sha256
    	elif self.config["type"] == "sha384":
    	    self.config["type"] = hashlib.sha384
    	elif self.config["type"] == "md5":
    	    self.config["type"] = hashlib.md5
    	elif self.config["type"] == "sha224":
    	    self.config["type"] = hashlib.sha224
    	elif self.config["type"] == "sha1":
    	    self.config["type"] = hashlib.sha1
    	elif self.config["type"] == "sha3_512":
    	    self.config["type"] = hashlib.sha3_512
    	elif self.config["type"] == "sha3_256":
    	    self.config["type"] = hashlib.sha3_256
    	elif self.config["type"] == "sha3_224":
    	    self.config["type"] = hashlib.sha3_224
    	elif self.config["type"] == "sha3_384":
    	    self.config["type"] = hashlib.sha3_384

    def findhashType(self):
    	if len(self.config["hash"])==32:
    	    return "md5"
    	elif len(self.config["hash"])== 40:
    	    return "sha1"
    	elif len(self.config["hash"]) == 64:
    	    return "sha256"
    	elif len(self.config["hash"]) == 128:
    	    return "sha512"
    	elif len(self.config["hash"]) == 56:
    	    return "sha224"
    	elif len(self.config["hash"]) == 96:
    	    return "sha384"
    	else:
    	    return "Cannot Be Determined "
    	
    def getexactHash(self,comp):
    	try:
    	    comp = comp.encode()
    	except:
    	    pass
    	return self.config["type"](comp).hexdigest()
    def cracktheHash(self,word):
    	compare = self.getexactHash(word)
    	
    	if str(compare) == str(self.config["hash"]):
    		try:
    		    print(self.G+"\n [ + ] Hash Cracked : ",word.decode(),self.N)
    		except:
    		    print(self.G+"\n [ + ] Hash Cracked : ",word,self.N)
    		self.Found = True
    		
    def killProc(self):
    	print("[ ! ] Wait For the script to stop")
    	if self.config["os"] == "linux":
    	    os.system(f"kill -9 {os.getpid()}")
    	else:
    	    os.system(f"taskkill /pid {os.getpid()} /f")
    def main(self):
    	if self.configureArgs():
    	    print("\n[ + ] Dictonary Approach")
    	    sleep(0.5)
    	    print("\n[ + ] Reading File ...")
    	    List = self.loadWordlist()
    	    self.returnhash()
    	   
    	    sleep(0.5)
    	    self.cls()
    	    print(self.Y)
    	    self.renderBanner("hash cracker")
    	    self.renderBanner("Mr Whitehat")
    	    print(self.N)
    	    Guess = self.findhashType()
    	    print("*"*130)
    	    print("\n[ * ] Hash : ",self.config["hash"])
    	    print("\n[ * ] Hash Guessed :",Guess)
    	    print("\n[ * ] Wordlist Locked :",self.config["wordlist"])
    	    print("\n[ * ] Word Count :",len(List))
    	    print("\n[ * ] Operating System FingerPrint :",self.config["os"])
    	    print("\n")
    	    print("*"*130)
    	    
    	    sleep(0.5)
    	    print(" # [ Info ] Cracking Hash Started ")
    	    try:
    	    	for words in List:
    	    	    if not self.Found:
    	    	       
    	    	        t = threading.Thread(target=self.cracktheHash,args=(words.strip(),),daemon=True)
    	    	        t.start()
    	    	        t.join()
    	    	    else:
    	    	    	break
    	    	sleep(0.5)
    	    except KeyboardInterrupt:
    	    	self.killProc()
    	    print(self.R+"\n[ * ] Finished")
    	    self.killProc()
d = cracker()

d.main()
