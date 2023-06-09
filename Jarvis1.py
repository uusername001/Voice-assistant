import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=15:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("Hello sir I am jarvis,how may i help you")


def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("say that again please")
        return "None"
    return query

wishme()
if __name__ =="__main__":
    while True:
        query= takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'name' in query:
            speak("My name is jarvis")
        elif 'what can you do' in query:
            speak("i can perform various tasks for you such as opening various websites or playing music or search wikipedia for information")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
        elif 'open w3schools' in query:
            webbrowser.open("w3schools.com")
        elif 'open wikipedia' in query:
            webbrowser.open("wikpedia.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'play music' in query:
            music_dir="C:\\music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'open code' in query:
            codepath="C:\\Users\\Hari\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        else:
            speak("apologies your query was not clear or not available, would you like to open any other websites such as google or spotify? ")
        
        
        



       
        

            

    

    


