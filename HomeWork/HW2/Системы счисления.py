import string

# Создается строка digits, объединяя все цифры и буквы верхнего регистра. Это будет использоваться для
# представления цифр в системах счисления с основанием больше 10
digits = string.digits + string.ascii_uppercase


# Определение функции convert_to_decimal, которая преобразует число num из системы счисления с основанием base_in в
# десятичную систему. Функция возвращает целое число
def convert_to_decimal(num: str, base_in: int) -> int:
    decimal_num = 0

    # Начало цикла
    for i, n in enumerate(num):
        # Добавление к decimal_num значения, представляющего текущую цифру, умноженную на соответствующую степень
        # основания
        decimal_num += digits.index(n.upper()) * (base_in ** (len(num) - i - 1))
    return decimal_num  # Возврат полученного десятичного числа


# Определение функции convert_from_decimal, которая преобразует число num из десятичной системы в другую систему
# счисления с основанием base_out. Функция возвращает строку
def convert_from_decimal(num: int, base_out: int) -> str:
    # Инициализация списка out_num_list для хранения результата преобразования обратно в другую систему
    out_num_list = []

    # Начало цикла, который выполняется, пока num не станет равным 0
    while num:
        # Добавление в out_num_list остатка от деления num на base_out, затем обновление num делением на base_out
        out_num_list.append(digits[num % base_out])
        num //= base_out
    # Возврат строки, полученной объединением элементов out_num_list в обратном порядке
    return ''.join(out_num_list[::-1])


# Определение функции summation, которая складывает два числа (num1 и num2) из системы счисления с основанием base_in
# и возвращает результат в системе счисления с основанием base_out
def summation(base_in: int, num1: str, num2: str, base_out: int) -> str:
    # Вызов функций convert_to_decimal для преобразования num1 и num2 в десятичную систему, их сложение, а затем вызов
    # convert_from_decimal для преобразования результата обратно в нужную систему счисления
    return convert_from_decimal(convert_to_decimal(num1, base_in) +
                                convert_to_decimal(num2, base_in), base_out)


# Проверка работы функций для нескольких тестов
if __name__ == '__main__':
    assert summation(2, '10', '10', 8) == '4', "2, '10', '10', 8 -> 4 [ERROR]"
    print("2, '10', '10', 8 -> 4 [PASSED]")

    assert summation(16, 'a', 'a', 10) == '20', "16, 'a', 'a', 10 -> 20 [ERROR]"
    print("16, 'a', 'a', 10 -> 20 [PASSED]")

    assert summation(10, '100', '100', 16) == 'C8', "10, '100', '100', 16 -> C8 [ERROR]"
    print("10, '100', '100', 16 -> C8 [PASSED]")

    assert summation(2, '101', '110', 16) == 'B', "2, '101', '110', 16 -> 10100 [ERROR]"
    print("2, '101', '110', 16 -> 10100 [PASSED]")
