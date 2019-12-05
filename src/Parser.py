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
		if self.__fileName != fileName:
			self.__fileName = fileName.replace("\\ ", " ").replace("\ ", " ").replace(" ", "\ ")
			# # self.__fileName = "\"" + fileName.replace("\\ ", " ").replace("\ ", " ") + "\""
			# fileName = fileName.replace("\\ ", " ")
			# fileName = fileName.replace("\ ", " ")
			# fileName = fileName.replace(" ", "\ ")
			# self.__fileName = fileName
			os.system("{}{}".format(self.__cmd, self.__fileName))

			file = open(self.__tmpFile, 'r')
			content = file.read()
			file.close

			return content.split('\n');
		
		else:
				return self.__fileName

	# Pas encore testé.
	def abstract(self, content):
		result = []
		successiveLineFeed = 0
		inAbstact = False	# True si la ligne courante est après le début du résumé.
		firstLine = 0;		# Premiere ligne du résumé. Utile pour déterminer la zone contenant le titre (entre ).

		for line in content:
			if not inAbstact:
				# match = re.search("[Aa]bstract[—-\. ]", content)
				match = re.search("abstract", line.lower())
				if match != None :
					inAbstact = True
					span = match.span()
					result.append(line[span[1]:].strip())

			else:
				# La line appartient peut-être au résumé.
				if line == "" and (len(result) > 1 or len(result) == 1 and result[0] != ""):	# Saut de ligne, donc, fin du résumé.
					break

				if line == "" and len(result) == 1 and result[0] == "":	# Saut de ligne en début de résumé.
					continue
				
				# Sinon, la ligne est dans le résumé.
				if line != result[-1] and line.lower().strip() != "abstract":
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
			if line == "" and result != "":	# Saut de ligne, donc, fin du titre.
				break
			else:
				result = " ".join([result, line])
		return [result.strip()]

	def author(self,content):
		fullTitle = self.title(content)
		authors = ""
		successiveLineFeed = 0
		partialAuthor = self.__fileName.split("_",1)[0]
		print(fullTitle)
		for line in content:
			match = re.search(fullTitle, line)
			
			if match != None :
				span = match.span()
				authors = line[span[1]:]
				break
				if line == "" and authors != "":	# Saut de ligne, donc, fin du titre.
					return authors.strip()
					break
		return partialAuthor

	def authorAddress(self,content):
		authors = self.author(content)
		address = ""
		successiveLineFeed = 0
		for line in content:
			match = re.search(authors, line.lower())
			if match != None :
				address = line
				while re.search("abstract", line.lower()) == None :
					address += line
			if line == "" and address != "":	# Saut de ligne, donc, fin du titre.
				break
			else:
				address = " ".join([address, line])
		return address.strip()

	def __del__(self):
		os.system("rm {}".format(self.__tmpFile))

	def parse(self, fileName):
		content = self.extractText(fileName)

		txt = {}	# Dictionnaire de listes.
		txt["preamble"] = [os.path.basename(self.__fileName).replace('\\','').strip()]
		txt["auteur"] = ""
		# txt["auteur"] = self.author(content) + " (" + self.authorAddress(content) + ")"
		txt["titre"] = self.title(content)
		txt["abstract"] = self.abstract(content)
		txt["biblio"] = ""

		return txt

	def parseTxt(self, fileName):
		txt = self.parse(fileName)

		xmlContent = []

		for key in txt.keys():
			xmlContent.append(key + " :")
			for line in txt[key]:
				xmlContent.append("\t" + line)

		return "\n".join(xmlContent)

	def parseXML(self, fileName):
		txt = self.parse(fileName)

		xmlContent = []
		header = ["<?xml version=\"1.0\" encoding=\"UTF-8\"?>", "<article>"]
		footer = "</article>"

		xmlContent.extend(header)

		for key in txt.keys():
			xmlContent.append("\t<" + key + ">")
			for line in txt[key]:
				xmlContent.append("\t\t" + line)
			xmlContent.append("\t</" + key + ">")
		
		xmlContent.append(footer)

		return "\n".join(xmlContent)


