import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import random

# ═══════════════════════════════════════════════════════════
#           VOICE ASSISTANT — OASIS INFOBYTE PROJECT 1
#           Built with Python | By: [Your Name]
# ═══════════════════════════════════════════════════════════

# ─────────────────────────────────
# PERSONALIZATION — Change to your name!
# ─────────────────────────────────
USER_NAME = "Srikar"  # ← Change this to YOUR name!

# ─────────────────────────────────
# SETUP SPEECH ENGINE
# ─────────────────────────────────
engine = pyttsx3.init('sapi5')          # Windows speech engine (sapi5)
engine.setProperty('rate', 170)         # Speech speed (170 = natural pace)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 = Male, 1 = Female


# ═══════════════════════════════════════════════════════════
#                     CORE FUNCTIONS
# ═══════════════════════════════════════════════════════════

def speak(text):
    """Convert text to speech and speak it out loud."""
    print(f"🤖 Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to microphone and convert speech to text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening...")

        # Filter out background noise before listening
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # Listen and capture audio (timeout after 5 seconds)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("🔄 Recognizing...")

        # Use Google's free speech recognition API (requires internet)
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"✅ You said: {query}")
        return query.lower()  # Return in lowercase for easy comparison

    except sr.UnknownValueError:
        # Could not understand the audio
        speak("Sorry, I didn't catch that. Please say it again.")
        return None

    except sr.RequestError:
        # Internet connection issue
        speak("I am having trouble connecting to the internet.")
        return None

    except sr.WaitTimeoutError:
        # No voice detected within timeout
        speak("I didn't hear anything. Please try again.")
        return None


# ═══════════════════════════════════════════════════════════
#                   FEATURE FUNCTIONS
# ═══════════════════════════════════════════════════════════

def greet_user():
    """Greet the user personally based on time of day."""
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    speak(f"{greeting}, {USER_NAME}! I am your personal voice assistant. How can I help you today?")


def tell_time():
    """Get and speak the current time."""
    # Format: 10:30 AM
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def tell_date():
    """Get and speak the current date."""
    # Format: April 09, 2026
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")


def search_wikipedia(query):
    """Search Wikipedia and speak a short 2 sentence summary."""
    speak("Searching Wikipedia, please wait...")
    try:
        # Remove the word 'wikipedia' from the query before searching
        query = query.replace("wikipedia", "").strip()

        # Fetch 2 sentence summary from Wikipedia
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia...")
        speak(result)

    except wikipedia.exceptions.DisambiguationError:
        # Multiple results found — need more specific query
        speak("There are multiple results. Please be more specific.")

    except wikipedia.exceptions.PageError:
        # No page found for the query
        speak("Sorry, I couldn't find anything on Wikipedia for that.")


def search_google(query):
    """Open Google search in the default browser."""
    # Remove trigger words from the query
    query = query.replace("search", "").replace("google", "").strip()

    # Build Google search URL and open it
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching Google for {query}")


def open_youtube(query):
    """Open YouTube search in the default browser."""
    # Remove 'youtube' keyword from the query
    query = query.replace("youtube", "").strip()

    # Build YouTube search URL and open it
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    speak(f"Opening YouTube for {query}")


def open_application(query):
    """Open common Windows applications based on voice command."""
    if "notepad" in query:
        speak("Opening Notepad!")
        os.system("notepad")                          # Opens Notepad

    elif "calculator" in query:
        speak("Opening Calculator!")
        os.system("calc")                             # Opens Calculator

    elif "camera" in query:
        speak("Opening Camera!")
        os.system("start microsoft.windows.camera:")  # Opens Camera

    elif "paint" in query:
        speak("Opening Paint!")
        os.system("mspaint")                          # Opens Paint

    elif "task manager" in query:
        speak("Opening Task Manager!")
        os.system("taskmgr")                          # Opens Task Manager

    else:
        speak("Sorry, I cannot open that application yet.")


def tell_random_fact():
    """Speak a random interesting fact."""
    facts = [
        "Honey never spoils. Archaeologists found 3000 year old honey in Egyptian tombs and it was still edible!",
        "A group of flamingos is called a flamboyance.",
        "Octopuses have three hearts and blue blood.",
        "The Eiffel Tower can be 15 centimetres taller during summer due to heat expansion.",
        "Bananas are berries, but strawberries are not!",
        "A day on Venus is longer than a year on Venus.",
        "Python programming language was named after Monty Python, not the snake!",
        "The first computer bug was an actual real bug, a moth found in a Harvard computer in 1947.",
        "Humans share 60 percent of their DNA with bananas.",
        "The average person walks about 100,000 miles in their lifetime, enough to circle the Earth 4 times!"
    ]

    # Pick a random fact from the list
    fact = random.choice(facts)
    speak("Here is an interesting fact for you!")
    speak(fact)


def tell_joke():
    """Speak a random programming or fun joke."""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the programmer quit his job? Because he didn't get arrays!",
        "How do you comfort a JavaScript bug? You console it!",
        "Why do Java developers wear glasses? Because they don't C sharp!",
        "I told my computer I needed a break. Now it won't stop sending me Kit Kat ads."
    ]

    joke = random.choice(jokes)
    speak(joke)


# ═══════════════════════════════════════════════════════════
#                   COMMAND PROCESSOR
# ═══════════════════════════════════════════════════════════

def process_command(query):
    """
    Understand the voice command and call the right function.
    Returns True to keep running, False to stop the assistant.
    """

    # ── Time ──
    if "time" in query:
        tell_time()

    # ── Date ──
    elif "date" in query:
        tell_date()

    # ── Wikipedia Search ──
    elif "wikipedia" in query:
        search_wikipedia(query)

    # ── YouTube ──
    elif "youtube" in query:
        open_youtube(query)

    # ── Google Search ──
    elif "search" in query or "google" in query:
        search_google(query)

    # ── Open Applications ──
    elif "open" in query:
        open_application(query)

    # ── Random Fact ──
    elif "fact" in query or "random fact" in query:
        tell_random_fact()

    # ── User's Name ──
    elif "my name" in query or "who am i" in query:
        speak(f"You are {USER_NAME}, my favorite human!")

    # ── Greeting ──
    elif "hello" in query or "hi" in query:
        speak(f"Hello {USER_NAME}! How can I help you?")

    # ── How are you ──
    elif "how are you" in query:
        speak(f"I am doing great, thank you for asking {USER_NAME}! How can I help you?")

    # ── Who are you ──
    elif "who are you" in query or "what are you" in query:
        speak(f"I am {USER_NAME}'s personal voice assistant, built with Python!")

    # ── Joke ──
    elif "joke" in query:
        tell_joke()

    # ── Stop / Exit ──
    elif "stop" in query or "exit" in query or "quit" in query:
        speak(f"Goodbye {USER_NAME}! Have a great day!")
        return False  # Signal to stop the main loop

    # ── Unknown Command ──
    else:
        speak("I am not sure how to help with that. Try asking me the time, date, or to search something.")

    return True  # Signal to keep the assistant running


# ═══════════════════════════════════════════════════════════
#                       MAIN PROGRAM
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":

    # Greet the user when program starts
    greet_user()

    # Keep running until user says stop/exit/quit
    running = True
    while running:
        # Listen for a voice command
        query = listen()

        # If a command was heard, process it
        if query:
            running = process_command(query)
