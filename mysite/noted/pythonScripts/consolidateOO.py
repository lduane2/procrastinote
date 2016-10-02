# coding=utf-8
from os.path import join, dirname
import string
import sys
class consolidate():
    def __init__(self, mode, keyword=""):
        topp = 0
        currentp = ""
        currline = 2
        line2 = ""
        count = 0

        f1 = open(join(dirname(__file__), './consolidate.txt'), 'w+')
        with open(join(dirname(__file__), './rawText.txt'), 'r') as document:
            if mode==0: # sentense
                for lines in document:
                    if (lines.find(keyword) != -1):
                        f1.write(lines)
            elif mode==1: #autosum
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
            elif mode==2: #paragraph mode
                for lines in document:
                    if(len(lines) == 2):
                        #print currentp
                        if(currentp.find(keyword) != -1):
                            #print keyword
                            f1.write(currentp)
                        currentp = ""

                    else:
                        currentp += lines
            elif mode==3: #smart mode
                for lines in document:
                    if(topp == 3):
                        if(len(lines) == 2):
                            topp = 0
                        else:
                            f1.write(lines)
                        if(topp == 1):
                            if(lines.find(keyword) != -1):
                                topp = 3
                            else:
                                topp = 0
                        if(len(lines) == 2):
                            topp = 1
                        if (lines.find(keyword) != -1):
                            f1.write(lines)
            else: #none
                for lines in document:
                    f1.write(lines)

            f1.close()
