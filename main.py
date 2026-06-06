# Import the speech recognition library
import speech_recognition as sr

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait.")
        # Listen for 1 second to calibrate the energy threshold for ambient noise levels
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Listening... Speak now!")
        # Capture the audio from the microphone
        audio_data = recognizer.listen(source)

        try:
            print("Recognizing your speech...")
            # Use Google's free Web Speech API to convert the audio to text
            text = recognizer.recognize_google(audio_data)
            print(f"\n--- You said ---\n{text}\n-----------------")

        except sr.UnknownValueError:
            # This happens if the audio was unclear
            print("Sorry, I could not understand the audio. Please try again.")
        except sr.RequestError as e:
            # This happens if there is an internet connection issue
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Run the function
if __name__ == "__main__":
    speech_to_text()