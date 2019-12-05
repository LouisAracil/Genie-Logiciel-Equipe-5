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
		print(parser.parseTxt(file))
	
elif option == '-x':
	for file in glob.glob(path + '/*.pdf'):
		print(parser.parseXML(file))

elif option == '-h':
	print(help)

else :
	print(help)
