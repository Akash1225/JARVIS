import speech_recognition as sr
import wikipedia
import pyttsx3
import os
import datetime
import webbrowser
import random


class Jarvis:
    Listening = True

    @classmethod
    def init(cls):
        date = datetime.datetime.now()
        hr = date.hour

        if hr < 12:
            cls.speak("Good morning sir")
        elif hr > 12 and hr < 18:
            cls.speak("Good Afternoon sir")
        else:
            cls.speak("Good evening")

        cls.speak("How can i help you")
        print("How can i help you")

    @classmethod
    def listen(cls):
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening ...")

            # HANDLE UNKNOWN ERROR
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio)

                if text is None:
                    pass
                else:
                    cls.task(text)
                    print(text)
            except sr.UnknownValueError:
                print("Please say again ...")

    @classmethod
    def speak(cls, msg):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # set the voice speed
        engine.say(msg)
        engine.runAndWait()

    @classmethod
    def task(cls, text):
        text = text.lower()

        # clear the screen
        if "clear the screen" in text:
            os.system("cls")

        # exit the screen
        if "exit" in text:
            cls.Listening = False

        # open youtube
        if "open youtube" in text:
            webbrowser.open("https://www.youtube.com")

        if "open google" in text:
            webbrowser.open("https://www.google.com")

        if "open github" in text:
            webbrowser.open("https://www.github.com/")

        if "open stackoverflow" in text:
            webbrowser.open("https://www.stackoverflow.com/")

        if "open sanskriti" in text:
            webbrowser.open("www.sanskriti.edu.in")

        if "open code" in text:
            os.system("start code")

        if "open powershell" in text:
            os.system("start powershell")

        if text in "open excel":
            os.system("start excel")

        # searching queries
        if "search" in text:
            try:
                summary = wikipedia.summary(text, 4)
                print(summary)
                cls.speak(summary)
            except:
                cls.speak("sorry coundn't find it")

        # change color
        if "change colour" in text:
            os.system(f"color {random.randrange(0,7)}")
        if "reset colour" in text:
            os.system(f"color 7")

        # date and time
        if "date time" in text:
            d = datetime.datetime.now()
            print(d)
            cls.speak(d)

        # shutdown the computer
        if "shutdown" in text:
            os.system("shutdown /s")
