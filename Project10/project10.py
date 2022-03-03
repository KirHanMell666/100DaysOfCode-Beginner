
def result(num1:float, operation, num2:float):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

loop = True

while loop:
    num1 = float(input("Podaj pierwszą liczbę: "))
    operation = input("Jaka operacja ma zostać wykonana (+ - * /): ")
    num2 = float(input("Podaj drugą liczbę: "))

    print(f"{num1} {operation} {num2} = {result(num1, operation, num2)}")