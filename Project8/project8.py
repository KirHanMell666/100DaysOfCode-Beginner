import art


def encrypt(text, shift):
    output = ""
    for letter in text:
        pos = alphabet.index(letter)
        newPos = pos + shift
        if newPos >= len(alphabet):
            newPos -= len(alphabet)
        output += alphabet[newPos]
    print(output)


def decrypt(text, shift):
    output = ""
    for letter in text:
        pos = alphabet.index(letter)
        newPos = pos - shift
        output += alphabet[newPos]
    print(output)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

loop = True

print(art.logo)

while loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    again = input("Do again? ('yes' or 'no'): ")
    if again == "yes":
        pass
    else:
        loop = False
