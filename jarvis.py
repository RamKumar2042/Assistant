import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import googlesearch  # pip install google
import webbrowser as wb
from googlesearch import search

import os
# import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'to google' in query:
            speak('Searching Goole')
            query=query.replace("Google","")
            results = googlesearch.summary(query, sentences = 2)
            speak('according to google0')
            print(results)
            speak(results)

        elif 'ram' in query:
            search("Google")

        elif 'open youtube' in query:
            speak("opening youtube")
            wb.open('https://www.youtube.com/')

        #  elif 'quit jarvis' in query:
        #    sys.exit()

        elif 'open google' in query:
            # webbrowser.open("google.com")
            speak("opening google")
            wb.open('www.google.com/')

        elif 'stack' in query:
            speak("opening stackoverflow")
            wb.open("www.stackoverflow.com")

        elif 'brio' in query:
            speak("opening Breo!")
            wb.open('https://breo.beds.ac.uk/')    

        elif 'open gmail' in query:
            speak("opening gmail!")
            wb.open('https://mail.google.com/mail/u/0/?tab=mm#inbox')    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            codePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        elif 'open browser' in query:
            codePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(codePath)

        elif'bye' in query:
            speak(" quiting jarvis program ! Good Byeee and have good day!")
            sys.exit()
