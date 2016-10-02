# coding=utf-8
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1



text_to_speech = TextToSpeechV1(
        username='5cf233f6-1bd1-4dd9-959e-7cbf72bd8d29',
        password='vLhtWWtffVLB'
        #x_watson_learning_opt_out=True
        )  # Optional flag




class speak():
    def __init__(self,filename):
        tmp = ""
        print '../media/'+filename
        with open(join(dirname(__file__), 'consolidate.txt'), 'r') as document:
            for line in document:
                tmp+=line
            with open('noted/media/'+filename, 'wb') as audio_file:
                audio_file.write(text_to_speech.synthesize(text=tmp, accept='audio/wav', voice="en-US_AllisonVoice"))
