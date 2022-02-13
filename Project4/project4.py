# Kamień, Papier, Nożyce
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choise = int(input("Wybierz 0 - kamień, 1 - papier, 2 - nożyce: "))
appChoice = random.randint(0, 2)

if appChoice == 0:
    print(rock)
    if choise == 0:
        print("remis")
    elif choise == 1:
        print("wygrana")
    else:
        print("przegrana")
elif appChoice == 1:
    print(paper)
    if choise == 0:
        print("przegrana")
    elif choise == 1:
        print("remis")
    else:
        print("wygrana")
else:
    print(scissors)
    if choise == 0:
        print("wygrana")
    elif choise == 1:
        print("przegrana")
    else:
        print("remis")
