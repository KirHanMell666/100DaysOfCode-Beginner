#Zadanie 1 - suma cyfr w 2-cyfrowej liczbie z inputu

x = input("Wpisz dwucyfrową liczbę: ")
x1 = int(x[0])
x2 = int(x[1])

print(x1 + x2)

#Zadanie 2 - obliczanie BMI

weight = int(input("Wpisz swoją wagę w kilogramach: "))
height = float(input("Wpisz swók wzrost z metrach: "))

print("Twoje BMI wynosi: " + str(weight/(height**2)))

#Zadanie 3 - Życie w tygodniach

age = int(input("Wpisz swój wiek: "))
EXPECTED_AGE = 90
remaining_years = EXPECTED_AGE - age
print("---------------------------------------------------------------------------------------")
print("Przy założeniu, że będziesz żył 90 lat pozostało ci: ")
print(str(remaining_years*365) + " dni | " + str(remaining_years*52) + " tygodni | " +
      str(remaining_years*12) + " miesięcy")
print("------------------------------------- Z użyciem \"f\" -----------------------------------")
days = remaining_years*365
weeks = remaining_years*52
months = remaining_years*12
print("Przy założeniu, że będziesz żył 90 lat pozostało ci: ")
print(f"{days} dni | {weeks} tygodni | {months} miesięcy")
