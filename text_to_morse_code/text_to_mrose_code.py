import time
import winsound
import platform

# Constants
DOT = '.'
DASH = '-'
LETTER_GAP = ' '
WORD_GAP = '/'

DOT_DURATION = 100
DASH_DURATION = 300
LETTER_GAP_DURATION = 0.3
WORD_GAP_DURATION = 0.7

# Morse code dictionary (all uppercase)
MORSE_CODE = {
    # Alphabets
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    # Numbers
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    # Special Characters
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

# Function to play Morse code
def play_morse(morse_text: str) -> None:
    for char in morse_text:
        if char == DOT:
            winsound.Beep(1000, DOT_DURATION)
        elif char == DASH:
            winsound.Beep(1000, DASH_DURATION)
        elif char == LETTER_GAP:
            time.sleep(LETTER_GAP_DURATION)
        elif char == WORD_GAP:
            time.sleep(WORD_GAP_DURATION)
        else:
            print(f"Unsupported Morse character: {char}")

# Function to convert text to Morse code
def text_to_morse(text: str) -> str:
    return ' '.join([MORSE_CODE.get(char.upper(), '') for char in text])

def main():
    # Check for platform compatibility
    if platform.system() != 'Windows':
        print("This program is intended for Windows.")
        return
    
    input_text = input('Enter text: ')
    morse_text = text_to_morse(input_text)
    print(f'Morse code: {morse_text}')
    
    make_sound = input('Make sound? (y/n): ')
    if make_sound == 'y':
        play_morse(morse_text)

if __name__ == '__main__':
    main()
