# coding=utf-8
import json
import os
from os import system
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1


text_to_speech = TextToSpeechV1(
    username='5cf233f6-1bd1-4dd9-959e-7cbf72bd8d29',
    password='vLhtWWtffVLB'
                                #x_watson_learning_opt_out=True
                                )  # Optional flag

print(json.dumps(text_to_speech.voices(), indent=2))

with open(join(dirname(__file__), '../resources/output.wav'), 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize(text='ACT I PROLOGUE Two households, both alike in dignity, In fair Verona, where we lay our scene, From ancient grudge break to new mutiny,  Where civil blood makes civil hands unclean. From forth the fatal loins of these two foes  A pair of star-crossd lovers take their life; Whose misadventured piteous overthrows Do with their death bury their parents strife.  The fearful passage of their death-markd love, And the continuance of their parents rage,  Which, but their childrens end, nought could remove,  Is now the two hours traffic of our stage; The which if you with patient ears attend,  What here shall miss, our toil shall strive to mend. SCENE I. Verona. A public place.', accept='audio/wav', voice="en-US_AllisonVoice"))

print(json.dumps(text_to_speech.pronunciation('Watson', pronunciation_format='spr'), indent=2))

print(json.dumps(text_to_speech.customizations(), indent=2))

#os.system('/usr/bin/afplay ../resources/output.wav')

# print(json.dumps(text_to_speech.create_customization('test-customization'), indent=2))

# print(text_to_speech.update_customization('YOUR CUSTOMIZATION ID', name='new name'))

# print(json.dumps(text_to_speech.get_customization('YOUR CUSTOMIZATION ID'), indent=2))

# print(json.dumps(text_to_speech.get_customization_words('YOUR CUSTOMIZATION ID'), indent=2))

# print(text_to_speech.add_customization_words('YOUR CUSTOMIZATION ID',
#                                              [{'word': 'resume', 'translation': 'rɛzʊmeɪ'}]))

# print(text_to_speech.set_customization_word('YOUR CUSTOMIZATION ID', word='resume',
#                                             translation='rɛzʊmeɪ'))

# print(json.dumps(text_to_speech.get_customization_word('YOUR CUSTOMIZATION ID', 'resume'), indent=2))

# print(text_to_speech.delete_customization_word('YOUR CUSTOMIZATION ID', 'resume'))

# print(text_to_speech.delete_customization('YOUR CUSTOMIZATION ID'))
