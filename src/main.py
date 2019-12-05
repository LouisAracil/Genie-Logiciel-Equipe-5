#!/usr/bin/env python3
# coding: utf-8

import os;
import glob;
import re;
import sys;
from Parser import *;

path = sys.argv[2]
# file = "../../Papers/Papers/Mikolov_2013_Distributed\ representations\ of\ words\ and\ phrases\ and\ their\ compositionality.pdf"
parser = Parser()

for file in glob.glob(path + '*.pdf'):



# file = parser.extractText(file);
# for line in file:
# 	print("\033[33m{}\033[0m".format(line))
		
# txt = parser.parse(file)

# print(
# 	"Nom du fichier :\n\t", 
# 	txt["name"],
# 	"\nTitre :\n\t", 
# 	txt["title"],
# 	"\nAbstract :\n", 
# 	"\t" + txt["abstract"][0] + "\n\t".join(txt["abstract"][1:]),
# 	end="\n\n")
	print("\n\n################################################################################\n################################################################################\n################################################################################\n\n")
	print(parser.parseTxt(file))
	print("\n--------------------------------------------------------------------------------\n")
	print(parser.parseXML(file))
	print("\n\n################################################################################\n################################################################################\n################################################################################\n\n")
