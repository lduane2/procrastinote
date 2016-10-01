# coding=utf-8
from os.path import join, dirname
import string

keyWord = "orange"
f1 = open(join(dirname(__file__), './consolidate.txt'), 'w+')
with open(join(dirname(__file__), './rawText.txt'), 'r') as document:
    for lines in document:
        if (lines.find(keyWord) != -1):
            f1.write(lines)


f1.close()
