class Stack:

    # Создается пустой список, который будет представлять стек
    def __init__(self):
        self.stack_list = []

    # Метод, который возвращает текущую длину стека
    def __len__(self):
        return len(self.stack_list)

    # Метод для извлечения элемента из вершины стека
    def pop(self):

        # Проверка, не пуст ли стек
        if len(self):
            # Извлечение и возвращение последнего элемента стека
            return self.stack_list.pop()
        else:
            # Если стек пуст, вызывается исключение IndexError
            raise IndexError('Empty Stack!')

    # Метод для добавления элемента на вершину стека
    def push(self, num: int):
        # Добавление элемента в конец стека
        self.stack_list.append(num)

    # Свойство для получения верхнего элемента стека без его извлечения. Возвращает последний элемент списка
    # (верхний элемент стека)
    @property
    def top_element(self):

        return self.stack_list[~0]


class Queue:
    # Инициализация объекта очереди с пустым списком
    def __init__(self):
        self.queue_list = []

    # Метод для получения длины очереди
    def __len__(self):
        return len(self.queue_list)

    # Метод для извлечения элемента из начала очереди
    def dequeue(self):
        # Проверка, не пуста ли очередь
        if len(self):
            # Извлечение и возвращение первого элемента очереди
            return self.queue_list.pop()
        else:
            # Если очередь пуста, вызывается исключение IndexError
            raise IndexError('Empty Queue!')

    # Метод для добавления элемента в конец очереди
    def enqueue(self, num: int):
        # Вставка элемента в начало списка (последний элемент очереди)
        self.queue_list.insert(0, num)

    # Свойство для получения первого элемента очереди без его извлечения
    @property
    def last_element(self):
        return self.queue_list[0]

    # Свойство для получения последнего элемента очереди без его извлечения
    @property
    def first_element(self):
        return self.queue_list[~0]


if __name__ == '__main__':
    # Создание объекта стека. Пример использования стека
    stack = Stack()
    # Добавление элементов 1, 2 и 3 в стек
    stack.push(1)
    stack.push(2)
    stack.push(3)
    # Вывод текущего состояния стека
    print(f"Stack: {stack.stack_list}")
    # Вывод верхнего элемента стека без извлечения
    print(f"Top Element: {stack.top_element}")
    # Извлечение элемента из вершины стека
    popped_element = stack.pop()
    # Вывод извлеченного элемента
    print(f"Popped Element: {popped_element}")
    # Вывод текущего состояния стека после извлечения
    print(f"Stack after pop: {stack.stack_list}")
    print()

    # Создание объекта очереди. Пример использования очереди
    queue = Queue()
    # Добавление элементов 1, 2 и 3 в очередь
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    # Вывод текущего состояния очереди
    print(f"Queue: {queue.queue_list}")
    # Вывод первого элемента очереди без его извлечения
    print(f"First Element: {queue.first_element}")
    # Вывод последнего элемента очереди без его извлечения
    print(f"Last Element: {queue.last_element}")
    # Извлечение элемента из начала очереди
    dequeued_element = queue.dequeue()
    # Вывод извлеченного элемента
    print(f"Dequeued Element: {dequeued_element}")
    # Вывод текущего состояния очереди после извлечения
    print(f"Queue after dequeue: {queue.queue_list}")
