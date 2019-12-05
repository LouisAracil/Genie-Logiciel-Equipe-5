#!/usr/bin/env python3
# coding: utf-8

import os;
import glob;
import re;
import sys;
from Parser import *;
 
path = sys.argv[2]
option = sys.argv[1]

parser = Parser()	

if option == '-t':
	for file in glob.glob(path + '/*.pdf'):
		print(file)
		print(parser.parseTxt(file))
	
elif option == '-x':
	for file in glob.glob(path + '/*.pdf'):
		print(parser.parseXML(file))

else :
	print("error")


