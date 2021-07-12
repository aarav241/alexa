from random import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
from twilio.rest import Client
import random
import sys
import pyautogui
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)

def talk(audio):
    print('Alexa: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        talk('Good Morning!')

    if currentH >= 12 and currentH < 18:
        talk('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        talk('Good Evening!')
        

greetMe()
time = datetime.datetime.now().strftime('%I:%M %p')
talk('Current time is ' + time)
talk('Hello Sir, I am your Alexa!')
talk('Now you can start using me.')

def take_command():
       
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        talk('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query

def run_alexa():
    while True:
        command = take_command()
        print(command)
        
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
            
        elif 'alexa' in command:
            call = command.replace('alexa','')
            
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            
        elif 'alarm' in command:
          talk('sir, i need a time to set alarm like , "set alarm to 2:18 a.m."')
          tt=take_command()
          tt= tt.replace("set alarm to","")
          tt= tt.replace(".","")
          tt= tt.upper()
          print(tt)
          import MyAlarm
          MyAlarm.alarm(tt)
            
        elif 'get me some information about' in command:
            person = command.replace('get me some information about', '')
            info = wikipedia.summary(person, 2)
            talk(info)
            print(info)
            
        elif 'tell me some thing about' in command:
            person = command.replace('tell me some thing about', '')
            info = wikipedia.summary(person, 2)
            talk(info)
            print(info)   
            
        elif 'joke' in command:
            talk(pyjokes.get_joke())
            
        elif 'open google' in command:
            talk('okay')
            webbrowser.open('www.google.com')
            
        elif 'what is the temperature in' in command:
            lis = command.replace('what is the temperature in','')
            search= "temperature in bihar"  
            url= f"https://www.google.com/serach?q={search}"
            r= requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp= data.find("div",class_="tempuret")
            talk(f"current {search} is {temp}")
            
        elif 'open white hat' in command:
            talk('okay sir, just a minute')
            webbrowser.open('code.whitehatjr.com')
            
        elif 'open code' in command:
            codePath = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open WhatsApp' in command:
            talk('yes sir, opening')
            Path = "C:\\Users\\lenovo\\AppData\\Local\\WhatsApp\\Whatsapp.exe"
            os.startfile(Path)
            
        elif 'open gmail' in command:
            talk('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in command or 'how are you' in command:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            talk(random.choice(stMsgs))

                                
        elif 'open spotify' in command:
            music_dir = 'C:\\Users\\lenovo\\AppData\\Roaming\\Spotify\\Spotify.exe'
            os.startfile(music_dir)
                    
            talk('yes sir, opening!')
            
        elif 'sleep' or 'exit' or 'stop' or 'abort' in command:
            talk('ok sir, thank\'s for using me.')
            sys.exit()
            
        else:
            talk('Please say the command again.')

# if __name__=="__main__":
while True:
 run_alexa()
#    command = take_command()
   
#    if 'wake up' in command:
#     talk(greetMe)
#    elif 'stop' in command:
#     talk('ok sir, thank\'s for using me.')
#     sys.exit()
