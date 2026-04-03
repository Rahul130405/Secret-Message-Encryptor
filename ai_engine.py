import os
from groq import Groq

def ai_guess_decryption(encrypted_text):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "Error: GROQ_API_KEY environment variable not set."

    client = Groq(api_key=api_key)

    prompt = f"""
You are an expert cryptanalyst. The following text is encrypted with a substitution cipher and a character swap cipher. The original text is in English. Analyze the encrypted text, try to decipher it, and provide the most likely original plaintext and your confidence in the guess as a percentage.

Encrypted text: "{encrypted_text}"

Please provide the output in the in the following format:
Guessed Plaintext: <your guess>
Confidence: <your confidence percentage>%
"""

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.1-8b-instant",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"