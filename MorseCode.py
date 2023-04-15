import winsound
import time

morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}




def decode_morse_code(encoded_text):
    encoded_text = encoded_text.split(' ')
    decoded_text = []
    for char in encoded_text:
        if char == '/':
            decoded_text.append(' ')
        else:
            for key, value in morse_code_dict.items():
                if char == value:
                    decoded_text.append(key)
    return ''.join(decoded_text)
