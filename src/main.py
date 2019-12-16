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

print("Quels fichiers voulez-vous parser ? (y/n)")
ok = ""
filesToParse = []
for file in glob.glob(path + '/*.pdf'):
	print('\t', file, sep='', end=' ')
	
	while True:
		ok = input()

		if ok.lower() in ['y', 'n', 'yes', 'no', 'oui', 'non', 'o']:
			break
		
		print("\t\tEntrée invalide. Choisissez entre 'y', 'n', 'yes', 'no', 'oui', 'non', 'o' : ", end='')
	
	if ok.lower() in ['y', 'yes', 'oui', 'o']:
		filesToParse.append(file)


parser = Parser()	

if option == '-t':
	for file in filesToParse:
		# print(parser.parseTxt(file))
		with open(file.replace(".pdf", ".txt"), 'w') as newFile:	# Pas besoin de fermer le fichier avec cette methode.
			newFile.write(parser.parseTxt(file))
	
elif option == '-x':
	for file in filesToParse:
		# print(parser.parseXML(file))
		with open(file.replace(".pdf", ".xml"), 'w') as newFile:
			newFile.write(parser.parseXML(file))

elif option == '-h':
	print(help)

else :
	print(help)
