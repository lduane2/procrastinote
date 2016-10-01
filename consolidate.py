# coding=utf-8
from os.path import join, dirname
import string
import sys
keyWord = "nonphysical"
pmode = 0
smart = 0
topp = 0
currentp = ""
f1 = open(join(dirname(__file__), './consolidate.txt'), 'w+')
with open(join(dirname(__file__), './dualism.txt'), 'r') as document:
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
					if(len(lines) == 1):
						topp = 0
					else:
						f1.write(lines)
				if(topp == 1):
					if(lines.find(keyword) != 1):
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
