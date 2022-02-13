# Zadanie 1 - średnia wzrostu

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0

for n in student_heights:
  sum += n

result = sum/len(student_heights)

print(round(result, 0))

# Zadanie 2 - wybranie maksymalnej wartości z inputu bez użycia funkcji max() i min()

print("-----------------------------------------------------")

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0

for i in student_scores:
  if max < n:
    max = n

print("Maksymalna podana wartość to: " + str(max))

# Zadanie 3 - suma liczb parzystych od 1 do 100

print("-----------------------------------------------------")

sum = 0
sum2 = 0

# 1 opcja
for i in range(1, 101):
  if i % 2 == 0:
    sum += i

# 2 opcja
for i in range(2, 101, 2):
  sum2 += i

print(sum, sum2)

# Zadanie 4 -

print("-----------------------------------------------------")

print("--- 1 opcja ---")

text = ""

# 1 wersja
for i in range(1, 101):
  text = i
  if i % 3 == 0:
    text = "Fizz"
  if i % 5 == 0:
    if text == "Fizz":
      text += "Buzz"
    else:
      text = "Buzz"
  print(text)

print("--- 2 opcja ---")

# 2 wersja
for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    text = "FizzBuzz"
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0:
    print("Fizz")
  else:
    print(i)