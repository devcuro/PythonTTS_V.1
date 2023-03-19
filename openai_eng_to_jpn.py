import openai

openai.api_key = "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" # Replace with your own API key

def translate(text):
    model_engine = "text-davinci-002" # Choose the language model to use
    prompt = f"translate English to Japanese: {text}"
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

# Example usage:
english_text = "Hello, how are you?"
japanese_translation = translate(english_text)
print(japanese_translation)
