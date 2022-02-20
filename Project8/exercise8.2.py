# Write your code below this line 👇
def prime_checker(number):
    pierwsza = True
    for i in range(2, int((number/2+1))):
        if number % i == 0:
            pierwsza = False
    if pierwsza:
        print("Podana liczna jest pierwsza")
    else:
        print("Podana liczna NIE jest pierwsza")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
