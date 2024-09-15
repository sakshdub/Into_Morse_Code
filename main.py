
# A text-based Python program to convert Strings into Morse Code.

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'  # Space character is often represented as '/'
}


def string_to_alphabet_list(input_string,morse_code_dict):
    # Use a list comprehension to filter out non-alphabet characters
    morse_code = []
    for char in input_string:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append("?")
    return ''.join(morse_code)


# Example usage
input_string = input("Enter a string: ").upper()
result = string_to_alphabet_list(input_string,morse_code_dict)
print(result)

