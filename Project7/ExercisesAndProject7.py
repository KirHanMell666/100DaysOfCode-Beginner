#Step 1
import random
import hangmanArt
import hangmanWords

def writeWord():
    global wordH, guess, wonB
    tmp = ""
    flag = True
    for x in wordH:
        if x in guess:
            tmp += x + " "
        else:
            tmp += "_ "
            flag = False
    if flag:
        won()
        wonB = True
    return tmp

def won():
    global loop
    loop = False
    print("Brawo, wygrałeś/aś!")


word = random.choice(hangmanWords.word_list)
wordH = []

for let in word:
    wordH.append(let)

guess = []
loop = True

print(hangmanArt.logo)

print(f"Słowo: {writeWord()}")

wonB = False
mistakes = 6

while loop:
    letter = input("Spróbuj zgadnąć literę: ").lower()
    if letter in guess:
        print("Wpisana litera była już wpisywana")
    else:
        guess.append(letter)
    if letter in word:
        print("# Prawidłowo #")
    else:
        print("# Błąd #")
        mistakes -= 1
    print(f"Słowo: {writeWord()}")
    if not wonB:
        print(f"Twoje wcześniejsze litery: {guess}")
        print(hangmanArt.stages[mistakes])
        if mistakes == 0:
            print("Przegrałeś! :(")
            print(f"Słowo, którego nie udało Ci się odgadnąć to: {word}")
            loop = False
        print("---------------------------------------------------------------")
