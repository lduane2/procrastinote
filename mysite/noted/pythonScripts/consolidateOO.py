# coding=utf-8
from os.path import join, dirname
import string
import sys
class consolidate(autosum, pmode, smart):
	def __init__(self):
		keyWord = "view"
		autosum = 1
		pmode = 0
		smart = 1
		topp = 0
		currentp = ""
		currline = 2
		line2 = ""
		count = 0
		f1 = open(join(dirname(__file__), './consolidate.txt'), 'w+')
		with open(join(dirname(__file__), './rawText.txt'), 'r') as document:
			if(autosum):
				for lines in document:
					if(count != 0):
						if(currline == 2):
							f1.write(lines)
							currline = 0
						if(len(lines) == 2):
							f1.write(line2)
							f1.write('\n')
							currline = 2
						line2 = lines
					else:
						count = 1
					
			if (pmode != 0):
				for lines in document:
					if(len(lines) == 1):
						#print currentp
						if(currentp.find(keyWord) != -1):
							print keyWord
							f1.write(currentp)
						currentp = ""
						
					else:
						currentp += lines
						#print lines
					#currentp = ""
			else:
				if(smart):
					for lines in document:
						if(topp == 3):
							if(len(lines) == 2):
								topp = 0
							else:
								f1.write(lines)
						if(topp == 1):
							if(lines.find(keyWord) != -1):
								topp = 3
							else:
								
								topp = 0
						if(len(lines) == 1):
							topp = 1
						if (lines.find(keyWord) != -1):
							f1.write(lines)
						
						
				else:
					for lines in document:
						if (lines.find(keyWord) != -1):
							f1.write(lines)


		f1.close()
