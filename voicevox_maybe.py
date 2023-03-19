#BROKEN
import asyncio
from voicevox import Client
import speech_recognition as sr
import openai


openai.api_key = "key-here" # Replace with your own API key


async def generate_voice():
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

        # Translate the input text to Japanese
        japanese_translation = translate(text, "Japanese")
        print(japanese_translation)

        async with Client() as voicevox_client:
            # Generate speech from the Japanese text
            speaker = 1
            speed = 1.0
            volume = 1.0
            tone = 0.0
            audio_query = await voicevox_client.create_audio_query(japanese_translation, speaker=speaker)
            voice = await audio_query.synthesis(speed=speed, volume=volume, tone=tone)
            with open("output.wav", "wb") as f:
                f.write(voice)
            print("Speech generated and saved to file.")

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
    asyncio.run(generate_voice())
