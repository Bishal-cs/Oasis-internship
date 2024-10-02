import os
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit as pw
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# For audio execution -------------------------------------------------
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Function to greet the user ------------------------------------------
def wish():
    hour = int(datetime.datetime.now().hour)
    speak("Hi, I am Edith.")

    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("How can I assist you, sir?")

# Function to take user input -----------------------------------------
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you repeat?")
            return None

# Main function for executing commands --------------------------------
if __name__ == "__main__":
    wish()
    while True:
        try:
            query = takecommand()

            if query is None:
                continue  # Wait for a valid command

            if "exit" in query:
                break

            elif "hello edit" in query or "hey edit" in query:
                speak("Hello! How can I assist you?")

            elif "wikipedia" in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            elif "play music" in query:
                speak("Which music you want to play? sir")
                query = takecommand().lower() + " on youtube"
                query = query.replace("play", "") 
                pw.playonyt(query)

            elif "open amazon" in query:
                webbrowser.open("amazon.com")

            elif "open github" in query:
                webbrowser.open("github.com")

            elif "open youtube" in query:
                webbrowser.open("youtube.com")

            elif"open notepad" in query:
                npath ="C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath)

            elif "open cmd" in query:
                os.system("start cmd")

            elif "open chrome" in query:
                webbrowser.open("chrome.com")

            elif "time" in query:
                speak("The current time is " + datetime.datetime.now().strftime("%H:%M %p"))

            elif "date" in query:
                speak("Today's date is " + datetime.datetime.now().strftime("%d"))

        except Exception as e:
            print(e)
