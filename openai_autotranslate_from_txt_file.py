import openai

openai.api_key = "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" # Replace with your own API key

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

# Read input text from a file
with open(r"C:\Users\cowsa\OneDrive\Desktop\openai_project_alpha\input.txt", "r") as f:
    english_text = f.read()

# Translate the input text to Japanese
japanese_translation = translate(english_text, "Japanese")
print(japanese_translation)

# Translate the Japanese text back to English
english_translation = translate(japanese_translation, "English")
print(english_translation)