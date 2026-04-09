import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import random

# I'm using sapi5 because it works well on Windows
# pyttsx3 helps me make the assistant speak
# speech_recognition is for listening to voice commands

my_name = "Bhavya"  # just change this to your name

# setting up the voice engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)  # not too fast, not too slow

# i tried both voices, female one sounds better to me
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    # this function makes the assistant talk
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    # this is where the assistant listens to what i say
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        # adjusting for background noise first
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=5)

    try:
        print("Let me think...")
        # sending audio to google to convert it to text
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry i didn't get that, can you say it again?")
        return None

    except sr.RequestError:
        speak("Hmm seems like there's no internet connection")
        return None

    except sr.WaitTimeoutError:
        speak("I didn't hear anything, are you there?")
        return None


def greet():
    # greeting based on what time of day it is
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak(f"Good morning {my_name}! what can i do for you today?")
    elif hour < 17:
        speak(f"Good afternoon {my_name}! how can i help you?")
    else:
        speak(f"Good evening {my_name}! what do you need?")


def get_time():
    # just telling the current time
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"its {now} right now")


def get_date():
    # telling today's date
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"today is {today}")


def search_wiki(command):
    # searching wikipedia and reading out a short summary
    speak("let me check wikipedia for that")
    try:
        query = command.replace("wikipedia", "").strip()
        result = wikipedia.summary(query, sentences=2)
        speak("ok so according to wikipedia")
        speak(result)

    except wikipedia.exceptions.DisambiguationError:
        speak("there are too many results for that, can you be more specific?")

    except wikipedia.exceptions.PageError:
        speak("hmm i couldn't find anything on wikipedia for that")


def open_google(command):
    # opening google with whatever they want to search
    query = command.replace("search", "").replace("google", "").strip()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"alright searching google for {query}")


def open_youtube(command):
    # opening youtube search
    query = command.replace("youtube", "").strip()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    speak(f"opening youtube for {query}")


def open_app(command):
    # opening some basic windows apps
    if "notepad" in command:
        speak("opening notepad!")
        os.system("notepad")

    elif "calculator" in command:
        speak("sure opening calculator")
        os.system("calc")

    elif "paint" in command:
        speak("opening paint for you")
        os.system("mspaint")

    elif "camera" in command:
        speak("opening camera")
        os.system("start microsoft.windows.camera:")

    elif "task manager" in command:
        speak("opening task manager")
        os.system("taskmgr")

    else:
        speak("sorry i don't know how to open that yet")


def random_fact():
    # i collected some fun facts that i find interesting
    facts = [
        "did you know honey never spoils? they found 3000 year old honey in egypt and it was still good!",
        "a group of flamingos is actually called a flamboyance, pretty cool right?",
        "octopuses have three hearts and their blood is blue",
        "the eiffel tower actually gets taller in summer because heat makes the metal expand",
        "bananas are technically berries but strawberries are not, crazy right?",
        "python was named after monty python the comedy show, not the snake!",
        "the first ever computer bug was a real moth stuck inside a harvard computer back in 1947",
        "humans share about 60 percent of their dna with bananas",
        "a day on venus is actually longer than a full year on venus"
    ]

    fact = random.choice(facts)
    speak("oh here's something interesting!")
    speak(fact)


def tell_joke():
    # some programming jokes i like
    jokes = [
        "why do programmers prefer dark mode? because light attracts bugs!",
        "why did the programmer quit? because he didn't get arrays!",
        "how do you comfort a javascript bug? you console it!",
        "why do java developers wear glasses? because they don't c sharp!"
    ]

    joke = random.choice(jokes)
    speak(joke)


def handle_command(command):
    # this is the main part that figures out what to do based on what was said

    if "time" in command:
        get_time()

    elif "date" in command:
        get_date()

    elif "wikipedia" in command:
        search_wiki(command)

    elif "youtube" in command:
        open_youtube(command)

    elif "search" in command or "google" in command:
        open_google(command)

    elif "open" in command:
        open_app(command)

    elif "fact" in command:
        random_fact()

    elif "joke" in command:
        tell_joke()

    elif "my name" in command or "who am i" in command:
        speak(f"you are {my_name} of course!")

    elif "hello" in command or "hi" in command:
        speak(f"hey {my_name}! what's up?")

    elif "how are you" in command:
        speak("i'm doing great thanks for asking! what do you need?")

    elif "who are you" in command or "what are you" in command:
        speak(f"i'm {my_name}'s personal assistant, made with python!")

    elif "stop" in command or "exit" in command or "quit" in command:
        speak(f"alright bye {my_name}, have a good one!")
        return False

    else:
        speak("hmm i'm not sure how to help with that, try asking me something else")

    return True


# this is where everything starts
if __name__ == "__main__":
    greet()

    running = True
    while running:
        command = listen()
        if command:
            running = handle_command(command)
