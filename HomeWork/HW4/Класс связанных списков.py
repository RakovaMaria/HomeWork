class Element:

    # Конструктор класса Element. Вызывается при создании нового объекта этого класса. Принимает один аргумент value,
    # который представляет собой значение элемента

    def __init__(self, value: int):
        self.value = value
        self.next_element = None


class LinkedList:

    # Конструктор класса LinkedList. Инициализирует пустой связанный список. Устанавливает атрибут first_element в None,
    # что означает, что список изначально пуст
    def __init__(self):
        self.first_element = None

    # Метод, который возвращает True, если связанный список пуст
    def is_empty(self):

        # Проверяет, есть ли у списка первый элемент
        return not self.first_element

    # Метод, который возвращает длину связанного списка
    def __len__(self):

        current_element = self.first_element
        length = 0
        # Цикл while для прохода по элементам списка, увеличивая счетчик length на каждом шаге
        while current_element:
            length += 1
            current_element = current_element.next_element
        return length

    # Метод, который проверяет, присутствует ли элемент с заданным значением num в связанном списке
    def search_element(self, num):

        current_element = self.first_element

        # Проходит по элементам списка с помощью цикла while и возвращает True, если элемент найден, и False, если
        # не найден
        while current_element:
            if current_element.value == num:
                return True
            current_element = current_element.next_element
        return False

    # Метод add_element добавляет новый элемент с заданным значением (num) в начало связанного списка
    def add_element(self, num):

        # Создание нового объекта класса Element с переданным значением num, который мы хотим добавить в связанный
        # список
        element_to_add = Element(num)
        # Установка указателя next_element нового элемента на текущий первый элемент списка
        element_to_add.next_element = self.first_element
        # Новый элемент становится первым в связанном списке
        self.first_element = element_to_add

    def remove_element(self, num):

        # Начало с первого элемента списка
        current_element = self.first_element
        # Инициализация переменной, которая будет содержать предыдущий элемент в процессе прохождения по списку
        previous_element = None

        # Цикл, который проходит по всем элементам списка
        while current_element:
            # Проверка, равно ли значение текущего элемента num. Если условие выполняется, то элемент найден
            if current_element.value == num:
                # Проверка, является ли найденный элемент первым в списке. Если это так, то обновляется атрибут
                # first_element так, чтобы он указывал на следующий элемент после найденного элемента
                if not previous_element:
                    self.first_element = current_element.next_element
                    return
                # Если найденный элемент не первый в списке, то обновляется указатель next_element предыдущего элемента
                # так, чтобы он указывал на следующий элемент после найденного элемента. Затем у найденного элемента
                # обнуляется указатель next_element, чтобы отсоединить его от списка
                else:
                    previous_element.next_element = current_element.next_element
                    current_element.next_element = None
                    return

            previous_element = current_element
            current_element = current_element.next_element

        print(f'Нет элемента {num} в списке')


if __name__ == '__main__':
    # Создание связанного списка
    linked_list = LinkedList()

    # Добавление элементов в связанный список
    linked_list.add_element(5)
    linked_list.add_element(10)
    linked_list.add_element(15)

    # Проверка, пуст ли связанный список
    print(f"Является ли связанный список пустым? {linked_list.is_empty()}")

    # Вывод длины связанного списка
    print(f"Длина связанного списка: {len(linked_list)}")

    # Поиск элементов в связанном списке
    print(f"Присутствует ли 10 в связанном списке? {linked_list.search_element(10)}")
    print(f"Присутствует ли 20 в связанном списке? {linked_list.search_element(20)}")

    # Удаление элементов из связанного списка
    linked_list.remove_element(10)
    print(
        f"Связанный список после удаления 10: Длина - {len(linked_list)}, Присутствует ли 10? "
        f"{linked_list.search_element(10)}")

    # Добавление еще элементов
    linked_list.add_element(25)
    linked_list.add_element(30)

    # Вывод конечного состояния связанного списка
    print(
        f"Конечный связанный список: Длина - {len(linked_list)}, Присутствует ли 15? {linked_list.search_element(15)}")
