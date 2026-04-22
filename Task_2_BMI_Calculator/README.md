# 🤖 Voice Assistant — Python Project

> A Python-based personal voice assistant that listens to your voice commands and responds intelligently!
> Built as part of the \*\*Oasis Infobyte Python Programming Internship\*\*.

\---

## 📋 Table of Contents

* [Demo](#demo)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [How to Run](#how-to-run)
* [Voice Commands](#voice-commands)
* [Project Structure](#project-structure)
* [Author](#author)

\---

## 🎬 Demo

> Record a short video of your assistant working and add the link here!

```
Video Demo: \[Add your LinkedIn/YouTube video link here]
```

\---

## ✨ Features

* 🎤 **Speech Recognition** — Listens to your voice using your microphone
* 🔊 **Text to Speech** — Speaks back responses out loud
* 🕐 **Time \& Date** — Tells the current time and date
* 🌐 **Google Search** — Opens Google search in your browser
* 📺 **YouTube Search** — Opens YouTube with your query
* 📖 **Wikipedia Search** — Reads a short Wikipedia summary
* 💻 **Open Applications** — Opens Notepad, Calculator, Paint, Camera
* 🎲 **Random Facts** — Tells interesting random facts
* 😄 **Jokes** — Tells random programming jokes
* 👤 **Personalized** — Greets you by your name

\---

## 🛠️ Technologies Used

|Technology|Purpose|
|-|-|
|Python 3.x|Core programming language|
|SpeechRecognition|Converting voice to text|
|pyttsx3|Converting text to speech|
|Wikipedia API|Fetching Wikipedia summaries|
|webbrowser|Opening browser for searches|
|datetime|Getting current time and date|
|os|Opening system applications|
|random|Selecting random facts/jokes|

\---

## ⚙️ Installation

**Step 1: Clone the repository**

```bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
```

**Step 2: Install required libraries**

```bash
pip install speechrecognition pyttsx3 wikipedia pyaudio requests
```

**⚠️ If PyAudio fails on Windows:**

```bash
pip install pipwin
pipwin install pyaudio
```

**Step 3: Verify installation**

```bash
python -c "import speech\_recognition, pyttsx3, wikipedia; print('All good!')"
```

\---

## ▶️ How to Run

**Step 1: Open the project folder**

```bash
cd voice-assistant
```

**Step 2: Change your name in the file**

```python
USER\_NAME = "YourName"  # Line 20 in voice\_assistant.py
```

**Step 3: Run the assistant**

```bash
python voice\_assistant.py
```

**Step 4: Speak a command when you see:**

```
🎤 Listening...
```

\---

## 🎙️ Voice Commands

|Say This|What Happens|
|-|-|
|`"What is the time"`|Tells the current time|
|`"What is the date"`|Tells today's date|
|`"Wikipedia Elon Musk"`|Reads Wikipedia summary|
|`"Search Python tutorial"`|Opens Google search|
|`"YouTube lo-fi music"`|Opens YouTube search|
|`"Open Notepad"`|Opens Notepad|
|`"Open Calculator"`|Opens Calculator|
|`"Open Paint"`|Opens Paint|
|`"Tell me a random fact"`|Speaks a random fact|
|`"Tell me a joke"`|Tells a joke|
|`"What is my name"`|Responds with your name|
|`"Hello"`|Greets you back|
|`"How are you"`|Assistant responds|
|`"Who are you"`|Describes itself|
|`"Stop / Exit / Quit"`|Closes the assistant|

\---

## 📁 Project Structure

```
voice-assistant/
│
├── voice\_assistant.py    # Main Python file
└── README.md             # Project documentation
```

\---

## 👤 Author

**Your Name**

* 🌐 GitHub: \[@Bhavyasree-katari](https://github.com/Bhavyasree-katari)
* 💼 LinkedIn: http://www.linkedin.com/in/%20bhavya-sree-katari-a36905295
* 📧 Email: kataribhvya217@gmail.com

\---

## 🏆 Internship

This project was built as part of the **Oasis Infobyte Python Programming Internship**.

**Hashtags:** #oasisinfobyte #oasisinfobytefamily #internship #python

\---

⭐ **If you found this helpful, please give it a star on GitHub!**

