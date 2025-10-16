import speech_recognition as sr
import webbrowser
import pyttsx3
import requests  # Make sure to import the requests module
import musicLibrary

# Initialize recognizer and engine objects
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# News API Key
newsapi = "3511262a7f874c9b919959e8b42327cc"

def speak(text):
    """Speaks the given text using the text-to-speech engine."""
    engine.say(text)
    engine.runAndWait()

# Create a sample music library (replace with your actual library)
musicLibrary = {
    "skyfall": "https://www.youtube.com/watch?v=rfuL-fDdkg0&list=RDrfuL-fDdkg0&start_radio=1",
    "song two": "https://www.youtube.com/watch?v=ApXoWvfEYVU&pp=ygUJc3VuZmxvd2Vy",
    "song three": "https://www.youtube.com/watch?v=CTFtOOh47oo&pp=ygUNdW5mb3JnZXR0YWJsZQ%3D%3D",
    "song four": "https://www.youtube.com/watch?v=DeumyOzKqgI&pp=ygUHc2t5ZmFsbA%3D%3D"
}

def process_command(command):
    """Processes the user's spoken command."""
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")

    elif command.startswith("play"):
        song = command.split()[1]
        if song in musicLibrary:
            link = musicLibrary[song]
            webbrowser.open(link)

    elif "news" in command:
        try:
            # Correct API request
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            r.raise_for_status()  # Raise an exception for bad status codes
            data = r.json()
            for article in data["articles"]:
                speak(article["title"])
        except requests.exceptions.RequestException as e:
            speak(f"Error fetching news: {e}")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            # Listen for the wake word "jarvis"
            print("Listening for wake word...")
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            if recognizer.recognize_google(audio).lower() == "jarvis":
                speak("Yes sir")

                # Listen for a command after Jarvis is activated
                print("Jarvis Active. Listening for command...")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                process_command(command)
        except Exception as e:
            print(f"Error: {e}")

#helloo














