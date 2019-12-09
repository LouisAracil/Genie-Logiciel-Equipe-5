#!/usr/bin/env python3
# coding: utf-8

import os;
import glob;
import re;
import sys;
from Parser import *;

help = "usage : py main.py [-t] [-x] path"


try:
	path = sys.argv[2]
	option = sys.argv[1]
except:
	print(help)
	exit()

parser = Parser()	

if option == '-t':
	for file in glob.glob(path + '/*.pdf'):
		# print(parser.parseTxt(file))
		with open(file.replace(".pdf", ".txt"), 'w') as newFile:	# Pas besoin de fermer le fichier avec cette methode.
			newFile.write(parser.parseTxt(file))
	
elif option == '-x':
	for file in glob.glob(path + '/*.pdf'):
		# print(parser.parseXML(file))
		with open(file.replace(".pdf", ".xml"), 'w') as newFile:
			newFile.write(parser.parseXML(file))

elif option == '-h':
	print(help)

else :
	print(help)
