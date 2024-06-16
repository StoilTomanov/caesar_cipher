from logo import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
if direction == 'encode':
    pass
elif direction == 'decode':
    alphabet.reverse()
else:
    raise ValueError('Invalid direction')
text = input("Type your message:\n").lower()
try:
    shift = int(input("Type the shift number: \n"))
except ValueError:
    raise ValueError('Invalid shift number')
shift = shift % 26


def caesar_cipher():
    translated_text = ''
    for char in text:
        if char not in alphabet:
            translated_text += char
            continue
        char_index_in_alphabet = alphabet.index(char)
        try:
            shifted_char = alphabet[char_index_in_alphabet + shift]
            translated_text += shifted_char
        except IndexError:
            alphabet.extend(alphabet)
            shifted_char = alphabet[char_index_in_alphabet + shift]
            translated_text += shifted_char
    print(translated_text)

caesar_cipher()