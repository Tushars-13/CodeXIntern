import speech_recognition as sr
import pyttsx3
import requests
import time

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command = recognizer.recognize_google(audio)
            print(f"User: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
            return ""

# Weather functionality
def get_weather(city):
    api_key = "67466b6ce432b700c887dd6d4923c608"  # MY OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url).json()
        
        if response.get("cod") == 200:
            weather = response["weather"][0]["description"]
            temp = response["main"]["temp"]
            speak(f"The weather in {city} is {weather} with a temperature of {temp} degrees Celsius.")
        else:
            error_message = response.get("message", "unknown error")
            speak(f"Sorry, I couldn't fetch the weather for {city}. Error: {error_message}")
    except requests.exceptions.RequestException as e:
        speak("There was an error connecting to the weather service. Please check your internet connection.")
        print(f"Error: {e}")


# News functionality
def get_news():
    api_key = "1fd15079734340c3976ef70e00a6beae"  # My newsAPI key
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    response = requests.get(url).json()

    if response.get("status") == "ok":
        articles = response["articles"][:5]
        speak("Here are the top headlines:")
        for i, article in enumerate(articles, 1):
            speak(f"{i}. {article['title']}")
    else:
        speak("Sorry, I couldn't fetch the news right now.")

# Reminder functionality
reminders = []

def set_reminder():
    speak("What should I remind you about?")
    reminder = listen()
    if reminder:
        reminders.append(reminder)
        speak(f"Reminder set: {reminder}")

def check_reminders():
    if reminders:
        speak("Here are your reminders:")
        for i, reminder in enumerate(reminders, 1):
            speak(f"{i}. {reminder}")
    else:
        speak("You have no reminders.")

# Main assistant loop
def main():
    speak("Hello! I am your voice-activated personal assistant. How can I help you today?")

    speak("I can tell you the correct time, can set your reminder, can check the weather and fetch the news for and you can give the command \'exit\' to exit ")
    
    while True:
        command = listen()

        if "weather" in command:
            speak("Which city?")
            city = listen()
            if city:
                get_weather(city)
        elif "news" in command:
            get_news()
        elif "reminder" in command:
            if "set" in command:
                set_reminder()
            elif "check" in command:
                check_reminders()
        elif "time" in command:
            current_time = time.strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")
        elif "exit" in command or "quit" in command:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("I'm sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()
