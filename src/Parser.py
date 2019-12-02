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
		txt["name"] = os.path.basename(self.__fileName).replace('\\','').strip()
		txt["title"] = self.title(content)
		txt["abstract"] = self.abstract(content)

		# name = os.path.basename(self.__fileName)
		# return name, self.title(content), self.abstract(content)
		return txt

	# Pas encore testé.
	def abstract(self, content):
		result = []
		successiveLineFeed = 0
		inAbstact = False	# True si la ligne courante est après le début du résumé
		firstLine = 0;		# Premiere ligne du résumé. Utile pour déterminer la zone contenant le titre (entre )

		for line in content:
			if not inAbstact:
				# match = re.search("[Aa]bstract[—-\. ]", content)
				match = re.search("abstract", line.lower())
				if match != None :
					inAbstact = True
					span = match.span()
					# result = "".join([result, match[span:]])	# Pas besoin de concaténantion car c'est le début du résumé. La variable est donc vide.
					result.append(line[span[1]:].strip())
			else:
				# La line appartient peut-être au résumé
				if line == "" and (len(result) > 1 or len(result) == 1 and result[0] != ""):	# Saut de ligne, donc, fin du résumé
											# len(result) == 1, car il faut, dans ce cas, qu'il n'y ait pas plus d'une ligne.
					break

				if line == "" and len(result) == 1 and result[0] == "":	# Saut de ligne, donc, fin du résumé
					continue
				
				# Sinon, la ligne est dans le résumé.
				if line != result[-1]:
					result.append(line.strip())
		
		return result


	def title(self, content):
		result = ""
		successiveLineFeed = 0
		partialTitle = self.__fileName
		partialTitle.split("_", 2)[2]

		for line in content:
			match = re.search(partialTitle, line.lower())
			if match != None :
				span = match.span()
				result = line[span[1]:]
			if line == "" and result != "":	# Saut de ligne, donc, fin du titre
				break
			else:
				result = " ".join([result, line])
		return result.strip()


	def __del__(self):
		os.system("rm {}".format(self.__tmpFile))

