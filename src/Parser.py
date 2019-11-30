#!/usr/bin/env python3
# coding: utf-8

import os;
import re;

class Parser:

	def __init__(self, tmpFileName = "tmp.txt"):
		self.__tmpFile = tmpFileName
		self.__fileName = ""
		self.__cmd = "pdf2txt -o {} ".format(self.__tmpFile)

		os.system("> {}".format(self.__tmpFile))

	def extractText(self, fileName):
		self.__fileName = fileName;
		os.system("{}{}".format(self.__cmd, fileName))

		file = open(self.__tmpFile, 'r')
		content = file.read()
		file.close

		return content.split('\n');

	def parse(self, fileName):
		content = self.extractText(fileName)

		txt = {}
		txt["name"] = os.path.basename(self.__fileName)
		txt["title"] = self.title(content)
		txt["abstract"] = self.abstract(content)

		# name = os.path.basename(self.__fileName)
		# return name, self.title(content), self.abstract(content)
		return txt

	# Pas encore testé.
	def abstract(content):
		result = ""
		successiveLineFeed = 0
		inAbstact = False	# True si la ligne courante est après le début du résumé
		firstLine = 0;		# Premiere ligne du résumé. Utile pour déterminer la zone contenant le titre (entre )

		for line in content:
			if not inAbstact:
				match = re.search("[Aa]bstract[—-\. ]", content)
				if match != None :
					inAbstact = True
					span = match.span()
					# result = "".join([result, match[span:]])
					result = match[span:]	# Pas besoin de concaténantion car c'est le début du résumé. La variable est donc vide.
			else:
				# La line appartient peut-être au résumé
				if re.search("^\s*$", content):	# Saut de ligne, donc, fin du résumé
					# if successiveLineFeed == 1:
					break

				# Sinon, la ligne est dans le résumé.
				result = " ".join([result, match[span:]])

	# Pas terminé.
	def title(content, headSpan):
		header = content
		if headSpan != None:
			header = content[:headSpan]	# Pour réduire zone de recherche afin de gagner en précision.

		pass
		# premier + saut de ligne si ':' MAIS manque : saut de ligne autrement et si pas 1er

		deletionList = [
#			"Available online at www.sciencedirect.com",	# Doit être pris en charge par un eexpression régulière.
			"Procedia.* [0-9]{3}–[0-9]{3}",
#			"www.elsevier.com/locate/procedia",
#			"November 17-19 2018, Dubai, United Arab Emirates",
			"[a-z]+\.[a-z\-_\.]\.[a-z]+\/?.*"
#			"www.elsevier.com/locate/procedia"
		]

	def __del__(self):
		os.system("rm {}".format(self.__tmpFile))

