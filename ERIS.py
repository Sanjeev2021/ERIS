import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyaudio
import os 
import smtplib
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning  sir")

        speak("I am ERIS . how may i help you ?")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")

        speak("I am ERIS . how may i help you ?")

    else:
        speak("Good Evening sir")

        speak("I am ERIS . how may i help you ?")

def takeCommand():
    #it take mircrophone inpt from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("sir please repeat that again....")
        speak("sir please repeat that again")
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('erisbot21@gmail.com', '9967492698')
    server.sendmail('erisbot21@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1 :
        query = takeCommand().lower()



    #Logic for executing task based on query
    if 'wikipedia' in query:
        speak("Getting info from wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=10)
        speak("Acoording to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open_new_tab("youtube.com")
        speak("Youtube open now")

    elif 'open google' in query:
        webbrowser.open_new_tab("google.com")
        speak("google opened ")

    elif 'open stackoverflow' in query:
        webbrowser.open_new_tab("stackoverflow.com")
        speak("Stackoverflow opened")

    elif 'open gmail' in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")

    elif 'open whatsapp' in query:
          webbrowser.open_new_tab("web.whatsapp.com")
          speak("Whatsapp opened")
            
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir , the time is {strTime}")
    
    elif 'send an email' in query:
        try:
            speak("what should i say?")
            content = takeCommand()
            to = "erisbot21@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent")
        except Exception as e :
            print(e)
            speak("sorry sir cannot send email")

    elif 'play music' in query:
        music_dir = 'F:\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir , songs[0]))
        
    
    elif "shutdown" in query:
            speak("Ok sir, your pc will log off in 10 seconds make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])  
    
    
