import string


# Функция convert_to_upper принимает текст txt и возвращает его верхний регистр
def convert_to_upper(txt):
    # Создаем словарь преобразования, заменяя каждую строчную букву на соответствующую заглавную
    convert_dict = str.maketrans(string.ascii_lowercase, string.ascii_uppercase)
    # Применяем словарь преобразования к тексту и возвращаем результат
    return txt.translate(convert_dict)


# Функция convert_to_lower принимает текст txt и возвращает его нижний регистр
def convert_to_lower(txt):
    # Создаем словарь преобразования, заменяя каждую заглавную букву на соответствующую строчную
    convert_dict = str.maketrans(string.ascii_uppercase, string.ascii_lowercase)
    # Применяем словарь преобразования к тексту и возвращаем результат
    return txt.translate(convert_dict)


# Функция mirror_convert принимает текст txt и отражает регистр в каждой букве
def mirror_convert(txt):
    # Создаем словарь преобразования, отражая регистр каждой буквы
    convert_dict = str.maketrans(string.ascii_uppercase + string.ascii_lowercase,
                                 string.ascii_lowercase + string.ascii_uppercase)
    # Применяем словарь преобразования к тексту и возвращаем результат
    return txt.translate(convert_dict)


if __name__ == "__main__":
    # Проверяем, что convert_to_upper работает корректно
    assert convert_to_upper("Hello") == "HELLO"
    print('1st test passed')

    # Проверяем, что convert_to_lower работает корректно
    assert convert_to_lower("WORLD") == "world"
    print('2nd test passed')

    # Проверяем, что mirror_convert работает корректно
    assert mirror_convert("Python") == "pYTHON"
    print('3rd test passed\n')
