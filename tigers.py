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
                                password='vLhtWWtffVLB'
                                #x_watson_learning_opt_out=True
                                )  # Optional flag


config = {'conversion_target': DocumentConversionV1.ANSWER_UNITS}

#
# Example with JSON
with open(join(dirname(__file__), './gsfinal.pdf'), 'r') as document:
    config['conversion_target'] = DocumentConversionV1.ANSWER_UNITS
    #print(json.dumps(document_conversion.convert_document(document=document, config=config), indent=2))
    hello = document_conversion.convert_document(document=document, config=config)
    print hello
    #print hello["answer_units"][0]["content"][0]["text"]
    hello2 = hello["answer_units"][0]["content"][0]["text"]
    print hello2
    printable = set(string.printable)
    hello2 = filter(lambda x: x in printable, hello2)
    hello2 = hello2.replace("*", "\n")
    print hello2
    hello2 = hello2.replace(".", "\n")
    #unicodedata.normalize( 'NFC', hello2).encode('ascii','ignore')
    #print hello2
with open(join(dirname(__file__), './rawText.txt'), 'w+') as odoc:
        odoc.write(" ")
        odoc.write(hello2)
        odoc.write("\n")
        odoc.close()



#with open(join(dirname(__file__), './output.wav'), 'wb') as audio_file:
#    audio_file.write(text_to_speech.synthesize(text=hello2, accept='audio/wav', voice="en-US_AllisonVoice"))
