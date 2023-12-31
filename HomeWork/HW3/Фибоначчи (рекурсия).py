def fibonacci(n):
    # Проверка, является ли n положительным целым числом
    if n <= 0:
        # Возвращение сообщения об ошибке при неверном вводе
        return "Неверный ввод"
    # Проверка, является ли n равным 1 или 2
    elif n == 1 or n == 2:
        # Возвращение 1 для первых двух членов последовательности Фибоначчи
        return 1
    else:
        # Рекурсивный вызов функции для вычисления n-го члена
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    # Получение ввода пользователя для определения n
    n = int(input("Введите номер члена последовательности Фибоначчи (n): "))

    # Вызов функции fibonacci для вычисления n-го члена
    result = fibonacci(n)

    # Вывод результата
    print(f"{n}-й член последовательности Фибоначчи: {result}")
