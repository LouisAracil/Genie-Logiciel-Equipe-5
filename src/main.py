#!/usr/bin/env python3
# coding: utf-8

import os;
import re;
import sys;
from Parser import *;

file = sys.argv[1]
# file = "../../Papers/Papers/Mikolov_2013_Distributed\ representations\ of\ words\ and\ phrases\ and\ their\ compositionality.pdf"
parser = Parser()

# file = parser.extractText(file);
# for line in file:
# 	print("\033[33m{}\033[0m".format(line))
		
txt = parser.parse(file)

print(
	"Nom du fichier :\n\t", 
	txt["name"],
	"\nTitre :\n\t", 
	txt["title"],
	"\nAbstract :\n", 
	"\t" + txt["abstract"][0] + "\n\t".join(txt["abstract"][1:]),
	end="\n\n")
