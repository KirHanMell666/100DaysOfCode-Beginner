players = {}
loop = True

while loop:
    name = input("Podaj swoje imie: ")
    bid = int(input("Ile zł oferujesz za ten przedmiot: "))
    players[name] = bid
    decision = input("Czy są jeszcze inni gracze? (tak/t | nie/n)").lower()
    if decision == "nie" or decision == "n":
        loop = False

maxV = 0
winner = ""

for value in players:
    if players[value] > maxV:
        maxV = players[value]
        winner = value

print(f"Zwycięzcą zostaje {winner}, który zapłaci {maxV}zł. Gratulacje!")
