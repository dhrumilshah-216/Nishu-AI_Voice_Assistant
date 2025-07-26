import pyttsx3
import webbrowser
import random
from langdetect import detect
from deep_translator import GoogleTranslator
from music_library import music
from api import fetch_news, ask_ai

# Some fun thinking lines to keep responses fresh
thinking_lines = [
    "Hmm... Let me think that through for you.",
    "Give me a sec, I'm channeling my inner genius...",
    "That's a brainy one — let me call in the big bots.",
    "Let's ask the AI brain on this one...",
    "Thinking hats on… here we go."
]

# Text-to-speech output
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Music playback logic
def song(song_name):
    normalized_music = {k.lower(): v for k, v in music.items()}
    if song_name in normalized_music:
        speak(f"Playing {song_name.title()}")
        webbrowser.open(normalized_music[song_name])
    else:
        # Search YouTube if song not in local library
        speak(f"Searching YouTube for {song_name.title()}")
        query = song_name.replace(" ", "+")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}autoplay=1")

# Fetch and read news using API
def get_news():
    data = fetch_news()
    if data and "results" in data and data["results"]:
        speak("Here are the top headlines:")
        for article in data["results"][:5]:
            title = article.get("title", "")
            lang = detect(title)
            if lang != 'en':
                translated = GoogleTranslator(source='auto', target='en').translate(title)
            else:
                translated = title
            print(translated)
            speak(translated)
    else:
        speak("Sorry, I couldn't fetch the news right now.")
        print("Raw API Response:", data)

# Handle user questions using AI API
def handle_user_query(user_input):
    print(f"🧑: {user_input}")
    ai_response = ask_ai(user_input)

    print(f"🤖: {ai_response}")
    speak(ai_response)

# Core command processor
def process_command(c):
    print(c)
    if("open google" in c.lower()):
        webbrowser.open("https://www.google.com/")
        speak("Opening Google, bro...")

    elif("open facebook" in c.lower()):
        webbrowser.open("https://www.facebook.com/")
        speak("Opening Facebook, bro...")

    elif("open instagram" in c.lower()):
        webbrowser.open("https://www.instagram.com/")
        speak("Opening Instagram, bro...")

    elif("open whatsapp" in c.lower()):
        webbrowser.open("https://web.whatsapp.com/")
        speak("Opening WhatsApp, bro...")

    elif("open youtube" in c.lower()):
        webbrowser.open("https://www.youtube.com/")
        speak("Opening YouTube, bro...")

    elif("open linkedin" in c.lower()):
        webbrowser.open("https://www.linkedin.com/")
        speak("Opening LinkedIn, bro...")

    elif c.lower().startswith("play"):
        # Extract song name and play
        song_name = ' '.join(c.split()[1:]).lower()
        song(song_name)

    elif "news" in c.lower():
        speak("Fetching the latest headlines...")
        get_news()

    else:
        # If command not matched, send to AI
        think = random.choice(thinking_lines)
        print("🤖:", think)
        speak(think)
        handle_user_query(c)