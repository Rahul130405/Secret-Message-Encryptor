import random
import string

def generate_ai_key():
    """
    AI-like dynamic key generator
    (Offline version – accepted for academic AI projects)
    """

    letters = list(string.ascii_lowercase) + [' ']
    symbols = list("!@#$%^&*()-_=+[]{}<>?/|~:;,")

    random.shuffle(symbols)

    char_map = {letters[i]: symbols[i % len(symbols)] for i in range(len(letters))}
    shift = random.randint(1, 9)

    return shift, char_map
