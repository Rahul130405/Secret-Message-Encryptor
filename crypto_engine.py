def swap_letters(message):
    if len(message) % 2 != 0:
        message += 'x'
    return ''.join(message[i+1] + message[i] for i in range(0, len(message), 2))

def obfuscate(text, shift, char_map):
    encrypted = ""
    for ch in text.lower():
        if ch in char_map:
            encrypted += char_map[ch]
        else:
            encrypted += str(ord(ch) + shift)
    return encrypted

def deobfuscate(text, shift, reverse_map):
    result = ""
    i = 0
    while i < len(text):
        if text[i] in reverse_map:
            result += reverse_map[text[i]]
            i += 1
        else:
            num = ""
            while i < len(text) and text[i].isdigit():
                num += text[i]
                i += 1
            if num:
                result += chr(int(num) - shift)
            else:
                result += text[i]
                i += 1
    return result
