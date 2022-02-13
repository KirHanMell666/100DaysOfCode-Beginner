#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for i in range(nr_letters):
    x = random.randrange(0, len(letters))
    password += letters[x]

for i in range(nr_symbols):
    x = random.randrange(0, len(symbols))
    password += symbols[x]

for i in range(nr_numbers):
    x = random.randrange(0, len(numbers))
    password += numbers[x]

print("Hasło ze znakami w kolejności litery -> symbole -> cyfry:")
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

list = []
passwordRandomized = ""

for i in password:
    list.append(i)
random.shuffle(list)

for i in list:
    passwordRandomized += i

print("Hasło z pomieszanymi znakami:")
print(passwordRandomized)