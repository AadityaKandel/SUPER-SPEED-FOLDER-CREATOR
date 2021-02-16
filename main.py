import os
from t1 import *

def createfolders(from_how_many,to_how_much):
	for i in range(from_how_many,to_how_much):
		try:
			os.mkdir(f'{i}')
		except:
			pass
	try:
		os.mkdir(f'{i+1}')
	except:
		pass

def deletefolders(from_how_many,to_how_much):
	for i in range(from_how_many,to_how_much):
		try:
			os.rmdir(f'{i}')
		except:
			pass
	try:
		os.rmdir(f'{i+1}')
	except:
		pass