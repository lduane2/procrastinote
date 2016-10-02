# coding=utf-8
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
        username='5cf233f6-1bd1-4dd9-959e-7cbf72bd8d29',
        password='vLhtWWtffVLB')

class speak():
    def __init__(self,filename):
        tmp = ""
        with open(join(dirname(__file__), 'consolidate.txt'), 'r') as document:
            for line in document:
                tmp+=line
            with open('noted/static/audio/'+filename, 'wb') as audio_file:
                audio_file.write(text_to_speech.synthesize(text=tmp, accept='audio/wav', voice="en-US_AllisonVoice"))
