#ControllerEnv
import os
import ctypes
import time
import requests

class offerRefuse:
	def __init__(self):
		self.inc = 1000000000

	# def malloc(self):
	# 	# TOO_MUCH_MEM = 100000000
	# 	# memdmp = ctypes.create_string_buffer(TOO_MUCH_MEM)
	# 	# if memdmp:
	# 	# 	ctypes.memset(memdmp, 0, TOO_MUCH_MEM)
	def millInc(self):
		counter = 0
		counter2 = 0
		for i in range(self.inc+1):
			counter+=1
			counter2+=1
			if (counter == self.inc) and counter2==self.inc:
				break
class detectSandBox:
	def __init__(self):
		self.url = "https://hckjofjodjfoCode.com/"
	def isUrlValid(self):
		try:
			response = requests.get(self.url)
			return True
		except:
			return False
		
s = detectSandBox()
print(s.isUrlValid())

