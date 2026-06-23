import os
import wikipedia
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
engine = pyttsx3.init()

while True:
 r = sr.Recognizer()

 with sr.Microphone() as source:
       print("Listening...")
       audio = r.listen(source)
 text = r.recognize_google(audio).lower()
 print("You said:", text)

 if "hello" in text:
    response = "Hello, how can I help you?"

 elif "time" in text:
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    response = "The time is " + current_time 

 elif "date" in text:
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    response = "Today's date is " + current_date

 elif "open google" in text:
     response = "opening Google"
     webbrowser.open("https://www.google.com")

 elif "open youtube" in text:
     response = "opening Youtube"
     webbrowser.open("https://www.youtube.com")

 elif "open linkedin" in text:
     response = "opening linkedIn"
     webbrowser.open("https://www.linkedin.com")

 elif "open calculator" in text:
    response = "Opening Calculator"
    os.system("calc")

 elif "notepad" in text:
    response = "Opening notepad"
    os.system("notepad")

 elif "search" in text:
    query = text.replace("search", "")
    response = " searching for "+ query
    webbrowser.open ("https://www.google.com/search?q=" + query)

 elif "who is" in text:
    person = text.replace("who is", "")
    try:
        info = wikipedia.summary(person, sentences=2)
        print(info)
        engine.say(info)
        engine.runAndWait()
    except:
        info = "Sorry, I could not find information."
        print(info)
        engine.say(info)
        engine.runAndWait()

 elif "what is" in text:
    topic = text.replace("what is", "").strip()
    try:
        response = wikipedia.summary(topic, sentences=2)
        print(response)
        engine.say(response)
        engine.runAndWait()
    except:
        response = "Sorry, I could not find information. "
        print(response)
        engine.say(response)
        engine.runAndWait()

 elif "stop" in text:
    response = "GOODBYE"
    print(response)
    engine.say(response)
    engine.runAndWait()
    break
 
 else:
    response = "Sorry, I do not understand."
    print(response)
    engine.say(response)
    engine.runAndWait()
