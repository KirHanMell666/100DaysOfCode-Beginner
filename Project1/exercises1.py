# Zadanie 1 i 2 - wypisywanie

print("----- Zadanie 1 i 2 - wypisywanie -----")

print("Aby wypisać coś na konsoli w Pythonie trzeba użyć funkcji: ")
print("print(\"tutaj wpisać co ma zostać wyświetlone\")")
print("Można również korzystać z apostrofów w cudzysłowach i na odwrót - 'przykład'")
print('Można również korzystać z apostrofów w cudzysłowach i na odwrót - "przykład"')
print("bez użycia \\\" lub \\\'")

# Zadanie 3 - input

print("----- Zadanie 3 - input -----")

print(input("Wpisz coś: "))
print(len(input("Tym razem wypiszemy jak wiele znaków ma tekst, który wpisałeś/aś (wraz ze spacją). Wpisz coś: ")))

# Zadanie 4 - zamiana wartości dwóch zmiennych liczbowych

print("----- Zadanie 4 - zamiana wartości -----")

print("Podaj 2 wartości dla zmiennej a oraz b")

a = input("a: ")
b = input("b: ")

temp = a
a = b
b = temp

print(f"Wartości zostały zamienione. a = {a}, b = {b}")