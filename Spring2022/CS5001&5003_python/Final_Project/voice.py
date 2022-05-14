"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Anything : ')
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, 2)
    try:
        text = r.recognize_google(audio, language='English')
        print('You said: {}'.format(text))
    except:
        print('Sorry, could not recognize your voice')

