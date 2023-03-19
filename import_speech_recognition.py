import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Define microphone as source
mic = sr.Microphone()

# Record audio from microphone
with mic as source:
    print("Speak now...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

# Convert speech to text
try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
