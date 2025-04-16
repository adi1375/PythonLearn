import os

def cls() -> None:
    os.system('cls' if os.name=="nt" else 'clear')

morse_code_dict: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/', '': " ",
    '&':'.-...', "'":'.----.', '@':'.--.-.', ')':'-.--.-', '(':'-.--.', ':':'---...', ',':'--..--', '=':'-...-', '!':'-.-.--', '.':'.-.-.-', '-':'-....-', '*':'-..-',
    '+':'.-.-.', '"':'.-..-.', '?':'..--..',
}

morse_code_reverse_dict = {v: k for k, v in morse_code_dict.items()}



def convert_to_morse(text: str) -> str:
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)

def morse_to_text(text: str) -> str:
    symbols: list[str] = text.split(" ")
    return ''.join(morse_code_reverse_dict[symbol] for symbol in symbols)

def main() -> None:
    cls()
    user_input: str = input("Enter text: ")
    output: str = convert_to_morse(user_input)
    print(output)
    reverse: str = morse_to_text(output)
    print(reverse)

if __name__ == '__main__':
    main()