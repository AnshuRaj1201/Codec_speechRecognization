# 🎙️ Speech to Text Converter

A simple yet powerful real-time **Speech-to-Text** application built with Python. It captures audio from your microphone, intelligently filters out background noise, and converts your speech into text using **Google's Web Speech API** — all in just a few lines of code.

> **Author:** Anshu Raj
> **Email:** anshuraj12012007@gmail.com

---

## ✨ Features

- 🎤 **Real-time microphone input** — No audio file needed; speak directly
- 🔇 **Ambient noise calibration** — Automatically adjusts to your environment
- 🌐 **Google Web Speech API** — High-accuracy speech recognition
- ⚠️ **Graceful error handling** — Handles unclear audio and connectivity issues

---

## 🛠️ How It Works

1. **Initializes** the speech recognizer
2. **Captures** live audio from the default microphone
3. **Calibrates** for 1 second to filter out background noise
4. **Listens** and records your speech
5. **Sends** the audio to Google's Speech Recognition API
6. **Prints** the transcribed text to the console

---

## 🧰 Tech Stack

| Library | Purpose |
|---|---|
| `SpeechRecognition` | Core speech-to-text functionality |
| `PyAudio` | Microphone access and audio stream handling |
| Google Web Speech API | Cloud-based speech recognition engine |

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/anshuraj/speech-to-text.git
cd speech-to-text
```

**2. Install dependencies**
```bash
pip install SpeechRecognition pyaudio
```

> **Note for Windows users:** If `pyaudio` fails to install, download the pre-built wheel from [PyAudio Wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install with:
> ```bash
> pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
> ```

> **Note for Linux users:**
> ```bash
> sudo apt-get install portaudio19-dev python3-pyaudio
> ```

> **Note for macOS users:**
> ```bash
> brew install portaudio
> pip install pyaudio
> ```

---

## 🚀 Usage

```bash
python main.py
```

Follow the prompts in the terminal:

```
Adjusting for background noise... Please wait.
Listening... Speak now!
Recognizing your speech...

--- You said ---
Hello, this is a speech to text test.
-----------------
```

---

## ⚠️ Error Handling

| Error | Cause | Message Shown |
|---|---|---|
| `UnknownValueError` | Audio was unclear or silent | `"Sorry, I could not understand the audio."` |
| `RequestError` | No internet / API issue | `"Could not request results from Google Speech Recognition service"` |

---

## 📋 Requirements

- Python 3.6+
- Working microphone
- Active internet connection (for Google Web Speech API)

---

## 🗂️ Project Structure

```
speech-to-text/
│
├── main.py       # Main speech recognition script
└── README.md     # Project documentation
```

---

## 🔮 Possible Improvements

- Save transcribed text to a `.txt` file automatically
- Add support for multiple languages
- Build a GUI using `Tkinter` or `PyQt`
- Integrate an offline recognition engine (e.g., `Vosk` or `Whisper`) for privacy
- Add continuous listening mode for longer conversations

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 📬 Contact

**Anshu Raj**
📧 [anshuraj12012007@gmail.com](mailto:anshuraj12012007@gmail.com)
