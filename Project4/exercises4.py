import random

# Zadanie 1 - orzeł czy reszka

headOrTails = random.randint(0, 1)
if headOrTails == 1:
    print("Orzeł")
else:
    print("Reszka")

# Zadanie 2 - losowanie osoby z wpisanej listy oddzielonej przecinkami

print("-----------------------------------------------------")

names_string = input("Podaj imiona wszystkich osób, oddzielając je przecinkami. ")
names = names_string.split(", ")

ran = random.randrange(0, len(names))
print(f"Dzisiaj zakupy robi: {names[ran]}")

# Zadanie 3 - listy w liscie, wybór punktu

print("-----------------------------------------------------")

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0]) - 1
row = int(position[1]) - 1

map[row][column] = "XX"

print(f"{row1}\n{row2}\n{row3}")
