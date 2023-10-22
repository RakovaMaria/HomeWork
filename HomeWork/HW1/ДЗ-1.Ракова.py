# Задача 1
F1 = 1
F2 = 1
n = int(input("N: "))
i = 0
while i < n - 2:
    F_sum = F1 + F2
    F1 = F2
    F2 = F_sum
    i = i + 1
print("N-ный элемент последовательности Фибоначчи:", F2)

# Задача 2
num = int(input("число: "))
prime = True
if num <= 1:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
if prime:
    print(num, "простое число")
else:
    print(num, "не простое число")

# Задача 3
num = int(input("число: "))
prime_divisors = []
for divisor in range(2, num):
    if num % divisor == 0:
        prime_divisors.append(divisor)
if not prime_divisors:
    print(num, "простое число.")
else:
    print(num, "простые делители:", prime_divisors)

# Задача 4
num1 = int(input("число 1: "))
num2 = int(input("число 2: "))
while num2:
    num1, num2 = num2, num1 % num2
print("НОД:", num1)

# Задача 5
side_length = int(input("число: "))
for i in range(side_length):
    for j in range(side_length):
        print("*", end=" ")
    print()

# Задача 6
w = int(input("ширина прямоугольника: "))
h = int(input("высота прямоугольника: "))
for i in range(h):
    for j in range(w):
        print("*", end=" ")
    print()

# Задача 7
l = int(input("длина прямоугольника: "))
h = int(input("высота прямоугольника: "))
number = 1
for i in range(h):
    for j in range(l):
        print(number, end=" ")
        number = number + 1
    print()
