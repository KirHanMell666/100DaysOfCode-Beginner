# Zadanie 1 - podział na liczby parzyste i nieparzyste

number = int(input("Podaj liczbę: "))

if number % 2 == 0:
    print("To liczba parzysta")
else:
    print("To liczba nieparzysta")

# Zadanie 2 - BMI 2.0

print("-----------------------------------------------------")

weight = int(input("Wpisz swoją wagę w kilogramach: "))
height = float(input("Wpisz swók wzrost z metrach: "))

bmi = weight/(height**2)

print(f"Twoje BMI wynosi: {bmi}")

if bmi <= 18:
    print("Niedowaga")
elif bmi <= 22:
    print("waga w normie")
elif bmi <= 28:
    print("Nadwaga")
elif bmi <= 33:
    print("Otyłość 1 stopnia")
else:
    print("Otyłość 2 stopnia")

# Zadanie 3 - sprawdzanie czy rok jest przestępny

print("-----------------------------------------------------")

year = int(input("Wpisz rok aby sprawdzić czy jest przestępny: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Rok jest przestępny")
        else:
            print("Rok nie jest przestępny")
    else:
        print("Rok jest przestępny")
else:
    print("Rok nie jest przestępny")

# Zadanie 4 - cennik pizzy

print("-----------------------------------------------------")

price = 0

small = 15
medium = 20
large = 25

pepperoniS = 2 #for small pizza
pepperoniML = 3 #for medium or large pizza
extraCheese = 1

size = input("Jaki rozmiar pizzy chcesz zamówić? S - mała, M - średnia, L - duża: ").upper()
pepperoni = input("Czy chcesz pizzę pepperoni? Y - tak, N - nie: ").upper()
cheese = input("Czy chcesz dodatkowy ser? Y - tak, N - nie: ").upper()
text = "Twoja pizza będzie Cię kosztować "

if size == "S":
    price += small
    if pepperoni == "Y":
        price += pepperoniS
elif size == "M":
    price += medium
    if pepperoni == "Y":
        price += pepperoniML
elif size == "L":
    price += large
    if pepperoni == "Y":
        price += pepperoniML
if cheese == "Y":
    price += extraCheese
print(text + str(price))

# Zadanie 5 - Kalkulator miłości

print("-----------------------------------------------------")

name1 = input("Podaj 1 imię: ")
name2 = input("Podaj 2 imię: ")
both = (name1 + name2).lower()

t = both.count("t")
r = both.count("r")
u = both.count("u")
e = both.count("e")

sumTrue = t + r + u + e
print(sumTrue)

l = both.count("l")
o = both.count("o")
v = both.count("v")
e = both.count("e") #nie ma znaczenia, że zmienna się powtarza.

sumLove = l + o + v + e
print(sumLove)

score = int(str(sumTrue) + str(sumLove))

if (score < 10) or (score > 90):
    print(f"Wynik miłości to {score}. Pasujecie do siebie jak cola i mentosy.")
elif (score <= 50) or (score >= 40):
    print(f"Wynik miłości to {score}. Powinniście być razem.")
else:
    print(f"Wynik miłości to {score}.")
