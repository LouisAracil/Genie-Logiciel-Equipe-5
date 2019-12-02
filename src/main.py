#!/usr/bin/env python3
# coding: utf-8

import os;
import re;
from Parser import *;


if __name__ == "__main__":
	files = [
		"../../Papers/Papers/Alexandrov_2015_A\ Modified\ Tripartite\ Model\ for\ Document\ Representation\ in\ Internet\ Sociology.pdf",
		"../../Papers/Papers/Doyle_2005_Automatic\ Categorization\ of\ Author\ Gender.pdf",
		"../../Papers/Papers/Furui_2004_Speech-to-text\ and\ speech-to-speech\ summarization\ of\ spontaneous\ speech.pdf",
		"../../Papers/Papers/Gonzalez_2018_Automated\ Sentence\ Boundary\ Detection\ in\ Modern\ StandardArabic\ Transcripts\ using\ Deep\ Neural\ Networks.pdf",
		"../../Papers/Papers/Levner_2007_Fuzzifying\ clustering\ algorithms\ The\ case\ study\ of\ MajorClust.pdf",
		"../../Papers/Papers/Lin_2004_Rouge.pdf",
		"../../Papers/Papers/Metsis_2006_Spam\ filtering\ with\ naive\ bayes-which\ naive\ bayes.pdf",
		"../../Papers/Papers/Mikolov_2013_Distributed\ representations\ of\ words\ and\ phrases\ and\ their\ compositionality.pdf",
		"../../Papers/Papers/Torres-Moreno_2012_Artex\ is\ another\ text\ summarizer.pdf",
		"../../Papers/Papers/Vanderwende_2007_Beyond\ SumBasic.pdf"
	]

	for file in files:
		# file = "../../Papers/Papers/Mikolov_2013_Distributed\ representations\ of\ words\ and\ phrases\ and\ their\ compositionality.pdf"
		parser = Parser()

		# file = parser.extractText(file);
		# for line in file:
		# 	print("\033[33m{}\033[0m".format(line))
		
		print(parser.parse(file), end="\n\n")
