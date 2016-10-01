# coding=utf-8
from os.path import join, dirname
import string
import sys
keyWord = "nonphysical"
pmode = 1
f1 = open(join(dirname(__file__), './consolidate.txt'), 'w+')
with open(join(dirname(__file__), './dualism.txt'), 'r') as document:
    if (pmode):
    	currentp = ""
    	for lines in document:
			if(len(lines) == 0):
				if(currentp.find(keyWord) != 1):
					f1.write(currentp)
				
			else:
				currentp += lines
			currentp = ""
	else:	
		for lines in document:
		    if (lines.find(keyWord) != -1):
		        f1.write(lilsnes)


f1.close()
