import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import musicLib
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="7b7e0d2f07da453dbfcd86bcc086ece1"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLib.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the json response
            data = r.json()
            #extract the articles
            articles = data.get('articles',[])
            # Print the headlines
            for article in articles:
                speak(article['title']) 
    else:
        #implementing openai
        pass
     

if __name__=="__main__":
    speak("Initializing Jarvis....")
    while True:
        # listen for jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using Sphinx
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()== "jarvis"):
                speak("Ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis is listening....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print(" error; {0}".format(e))

