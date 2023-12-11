# Запрашиваем основание первой системы счисления
base1 = int(input("Введите основание первой системы счисления: "))

# Запрашиваем первое число в первой системе счисления
num1_str = input("Введите первое число: ")

# Запрашиваем второе число в первой системе счисления
num2_str = input("Введите второе число: ")

# Запрашиваем основание второй системы счисления
base2 = int(input("Введите основание второй системы счисления: "))

# Инициализируем результат как 0
result = 0

# Конвертируем первое число в десятичное число в первой системе счисления
for digit in num1_str:
    result = result * base1 + int(digit)

# Инициализируем вспомогательную переменную для хранения второго числа в десятичной системе
num2_decimal = 0

# Конвертируем второе число в десятичное число в первой системе счисления
for digit in num2_str:
    num2_decimal = num2_decimal * base1 + int(digit)

# Выполняем сложение в десятичной системе счисления
decimal_result = result + num2_decimal

# Инициализируем строку для хранения результата во второй системе счисления
result_str = ""

# Переводим результат во вторую систему счисления
while decimal_result > 0:
    digit = decimal_result % base2
    result_str = str(digit) + result_str
    decimal_result //= base2

# Выводим результат
print(f"Результат в {base2}-й системе счисления: {result_str}")




import subprocess

# Шаг 1: Добавить изменения в коммит
subprocess.run(['git', 'add', '.'])

# Шаг 2: Сделать коммит
subprocess.run(['git', 'commit', '-m', 'Внесены изменения'])

# Шаг 3: Войти в свой аккаунт GitHub
subprocess.run(['git', 'config', '--global', 'user.email', 'm98535248@gmail.com'])
subprocess.run(['git', 'config', '--global', 'user.name', 'RakovaMaria'])

# Шаг 4: Повторить git push
subprocess.run(['git', 'push'])
