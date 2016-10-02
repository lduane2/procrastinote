# coding=utf-8
import json
from os.path import join, dirname
import string
from watson_developer_cloud import DocumentConversionV1, TextToSpeechV1

document_conversion = DocumentConversionV1(
        username='632d20d2-21d6-4b72-b1e4-35409db12fe3',
        password='nB2m1r40gUIi',
        version='2016-02-09')

text_to_speech = TextToSpeechV1(
        username='5cf233f6-1bd1-4dd9-959e-7cbf72bd8d29',
        password='vLhtWWtffVLB')

class tigers():
    def __init__(self,filename):
        config = {'conversion_target': DocumentConversionV1.ANSWER_UNITS}

        with open(filename, 'r') as document:
            config['conversion_target'] = DocumentConversionV1.ANSWER_UNITS
            hello = document_conversion.convert_document(document=document, config=config)
            hello2 = hello["answer_units"][0]["content"][0]["text"]
            printable = set(string.printable)
            hello2 = filter(lambda x: x in printable, hello2)
            hello2 = hello2.replace("*", "\n")
            hello2 = hello2.replace(".", "\n")
        with open(join(dirname(__file__), './rawText.txt'), 'w+') as odoc:
            odoc.write(" ")
            odoc.write(hello2)
            odoc.write(" \n")
            odoc.close()
