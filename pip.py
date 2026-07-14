import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
#initialize voice engine
engine = pyttsx3.init()

def speak(Text):
    engine.say(Text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening.")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("you said:",command)
        return command.lower()
    
    except Exception:
        print("sorry,please say that again..")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour
    
    if hour < 12:
        speak("good morning\nI am your virtual Assistant")
    elif hour < 18:
        speak("good afternoon \nI am your virtual Assistant")
    else:
        speak("good evening \nI am your virtual Assistant")

wish_user()

while True:
    
    command = take_command()
    
    if "time" in command:
        
        time = datetime.datetime.now().strftime("%I:%M %P")
        speak(f"the time is {time}")
        
    elif "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "open WhatsApp" in command:
        webbrowser.open("https://www.WhatsApp.com")

        
        

    elif "who is" in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person,2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("goodbye")
        break
