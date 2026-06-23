import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
engine = pyttsx3.init()
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
elif "search" in text:
    query = text.replace("search", "")
    response = " searching for "+ query
    webbrowser.open ("https://www.google.com/search?q=" + query)     
else:
    response = "Sorry, I do not understand."
print(response)
engine.say(response)
engine.runAndWait()