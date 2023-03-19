import speech_recognition as sr
import openai

openai.api_key = "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" # Replace with your own API key

# Initialize recognizer
r = sr.Recognizer()

# Define microphone as source
mic = sr.Microphone()

def transcribe_and_translate():
    # Record audio from microphone
    with mic as source:
        print("Speak now...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # Convert speech to text
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        # Write text to file
        with open(r"C:\Users\cowsa\OneDrive\Desktop\openai_project_alpha\recognized_text.txt", "w") as f:
            f.write(text)
            print("Recognized text written to file.")

        # Translate the input text to Japanese
        japanese_translation = translate(text, "Japanese")
        print(japanese_translation)

        # Translate the Japanese text back to English
        english_translation = translate(japanese_translation, "English")
        print(english_translation)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def translate(text, target_language):
    source_language = "English" if target_language == "Japanese" else "Japanese"
    model_engine = "text-davinci-002" # Choose the language model to use
    prompt = f"translate {source_language} to {target_language}: {text}"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    return message

if __name__ == "__main__":
    transcribe_and_translate()
