#this voice feature will work only in online mode for now
#the googletrans library need to be updated to the latest version for effective working of the program
from gtts import  gTTS
from googletrans import Translator
from playsound import playsound
import os
from datetime import datetime

filename=''
def voice(data):
    date_string=datetime.now().strftime("%d%m%Y%H%M%S")
    filename="voice"+date_string+".mp3"
    data=str(data)
    trans=Translator()
    t=trans.translate(data,dest="hi")
    print(t.text)
    language="hi"
    code=t.text
    output=gTTS(text=code,lang=language,slow=False)
    try:
        output.save(filename)
        while playsound(filename):
            pass
        os.remove(filename)

    except:
        pass

    return
