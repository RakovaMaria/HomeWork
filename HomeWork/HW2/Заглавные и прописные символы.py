# Задание 1
import string

# Входная строка
input_string = ("Буквы: abcdefghijklmnopqrstuvwxyz")

# Пустая строка для результата
result_string = ""

# Проходим по каждому символу во входной строке
for char in input_string:
    if char in string.ascii_lowercase:
        # Если символ является строчной буквой, добавляем его в результат как заглавную
        result_string += string.ascii_uppercase[string.ascii_lowercase.index(char)]
    else:
        # Если символ не является строчной буквой, добавляем его в результат как есть
        result_string += char

# Выводим строку с заглавными буквами
print("Преобразование в заглавные: ", result_string)




# Задание 2
import string

# Входная строка
input_string = "Буквы: abcABC"

# Пустая строка для результата
result_string_upper = ""
result_string_lower = ""

# Проходим по каждому символу во входной строке
for char in input_string:
    if char in string.ascii_lowercase:
        # Если символ является строчной буквой, добавляем его в результат как заглавную
        result_string_upper += string.ascii_uppercase[string.ascii_lowercase.index(char)]
    else:
        # Если символ не является строчной буквой, добавляем его в результат как есть
        result_string_upper += char

    if char in string.ascii_uppercase:
        # Если символ является заглавной буквой, добавляем его в результат как прописную
        result_string_lower += string.ascii_lowercase[string.ascii_uppercase.index(char)]
    else:
        # Если символ не является заглавной буквой, добавляем его в результат как есть
        result_string_lower += char

# Выводим строки
print("Преобразование в заглавные: ", result_string_upper)
print("Преобразование в прописные: ", result_string_lower)



