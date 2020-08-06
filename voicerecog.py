import speech_recognition as sr
import webbrowser

r= sr.Recognizer()
r.energy_threshold=5000
# r2= sr.Recognizer()
# r3 = sr.Recognizer()

sr.Microphone( device_index=1 )
r=sr.Recognizer()
r.energy_threshold=5000

with sr.Microphone() as source:

    print("speak!")
    audio= r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("you said : {}".format(text))
        url = 'https://www.google.co.in/search?q='
        search_url= url+text
        webbrowser.open(search_url)
    except:
        print("can't recognize")    

