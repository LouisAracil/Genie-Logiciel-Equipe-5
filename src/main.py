#!/usr/bin/env python3
# coding: utf-8

import os;
import re;
from Parser import *;


if __name__ == "__main__":
	parser = Parser()
	file = parser.extractText("../../Papers/Papers/Mikolov_2013_Distributed\ representations\ of\ words\ and\ phrases\ and\ their\ compositionality.pdf");

	for line in file:
		print("\033[33m{}\033[0m".format(line))
	

	print('ok')
