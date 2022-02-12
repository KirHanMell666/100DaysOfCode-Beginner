print("Witaj w kalkulatorze napiwków")
bill = float(input("Wpisz kwotę rachunku: "))
percentOfTip = float(input("Ile procent napiwku byś chciał dać? 10, 12 czy może 15? "))
multiplier = (percentOfTip/100.0) + 1
people = int(input("Ile osób płaci rachunek: "))
finalPricePerPerson = round(bill * multiplier / people, 3)
print(f"Każda z osób powinna zapłacić {finalPricePerPerson} zł.")
