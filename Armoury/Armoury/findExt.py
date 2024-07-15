#FindPS1
import os
import subprocess
import sys

def GetDrive():
	out = subprocess.getoutput("wmic logicaldisk get caption").split()[1:]
	return out
if len(sys.argv)==2:
	for d in GetDrive():
			for root,dirs,files in os.walk(d+"\\"):
				for file in files:
					if file.endswith(sys.argv[1]):
						print(os.path.join(root,file))
