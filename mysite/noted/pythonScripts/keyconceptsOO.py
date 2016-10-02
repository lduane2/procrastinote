import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='9bcf7ddbaeaeb6ab4edfac834e654c3d7bdf758a')

class keyconcepts():
    def __init__(self):
        p = ""
        with open(join(dirname(__file__), './rawText.txt'), 'r') as document:
            for line in document:
                p += line

        combined_operations = ['concept']

        f1 = open(join(dirname(__file__), './concepts.txt'), 'w+')
        jsonObject = alchemy_language.combined(text=p, extract=combined_operations, max_items=5)
        for thing in jsonObject['concepts']:
            f1.write(thing['text'])
            f1.write("\n")

        f1.close()
