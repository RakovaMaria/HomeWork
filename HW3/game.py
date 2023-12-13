# Модуль `math предоставляет математические функции, импорт абстрактного базового класса ABC и декоратора
# abstractmethod из модуля abc
import math
from abc import ABC, abstractmethod


# Конструктор класса Location с четырьмя параметрами: name, width, height и length
class Location:
    def __init__(self, name: str, width: int, height: int, length: int):
        self.name = name  # Устанавливает атрибут name для объекта Location
        self._width = width  # Устанавливает приватный атрибут _width для объекта Location
        self._height = height  # Устанавливает приватный атрибут _height для объекта Location
        self._length = length  # Устанавливает приватный атрибут _length для объекта Location
        self._objs = []  # Инициализирует список _objs, предназначенный для хранения объектов в данной локации

    # Определяется метод add_object, который добавляет объект в список _objs, если его там еще нет
    def add_object(self, obj):
        if obj not in self._objs:
            self._objs.append(obj)

    # Метод clear очищает список объектов _objs (ставит его в значение None)
    def clear(self):
        self._objs = None

    # Метод is_inside проверяет, находятся ли координаты внутри локации
    def is_inside(self, x, y, z) -> bool:
        return 0 < x < self._length and 0 < y < self._width and 0 < z < self._height

    # Каждая строка с аннотацией @property определяет свойство объекта, к которому можно обращаться, как к обычной
    # переменной, но при этом вызывается соответствующий метод
    @property
    def width(self):
        #  Свойство, возвращающее ширину объекта в локации
        return self._width

    @property
    def length(self) -> int:
        # Свойство, возвращающее длину объекта в локации
        return self._length

    @property
    def height(self):
        # Свойство, возвращающее высоту объекта в локации
        return self._height

    @property
    def volume(self):
        # Свойство, возвращающее объем объекта, рассчитанный как произведение длины, ширины и высоты
        return self.height * self.length * self.width


# Класс Location представляет собой простое пространство с заданными размерами. GameObject представляет объект в этом
# пространстве с координатами x, y, z.
class GameObject:
    def __init__(self, name: str, loc: Location, x, y, z):
        # Конструктор объекта. Принимает имя, локацию, и координаты x, y, z.
        self.name = name
        self._loc = loc
        self._loc.add_object(self)  # Добавляет текущий объект в список объектов локации
        self.x, self.y, self.z = x, y, z

    @property
    def x(self):
        # Свойство, возвращающее координату x объекта
        return self._x

    @x.setter
    def x(self, x):
        # Сеттер для координаты x, который устанавливает ее значение в зависимости от длины локации
        if x < 0:
            self._x = 0
        elif self._loc.length < x:
            self._x = self._loc.length
        else:
            self._x = x

    @property
    def y(self):
        # Аналогично x, свойство для координаты y
        return self._y

    @y.setter
    def y(self, y):
        # Сеттер для координаты y, который устанавливает ее значение в зависимости от ширины локации
        if y < 0:
            self._y = 0
        elif self._loc.width < y:
            self._y = self._loc.width
        else:
            self._y = y

    @property
    def z(self):
        # Аналогично x и y, свойство для координаты z
        return self._z

    @z.setter
    def z(self, z):
        # Сеттер для координаты z, который устанавливает ее значение в зависимости от высоты локации
        if z < 0:
            self._z = 0
        elif self._loc.height < z:
            self._z = self._loc.height
        else:
            self._z = z

    # Метод move класса GameObject предназначен для перемещения объекта в пространстве по заданным значениям x, y и z
    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    # dx, dy, dz: вычисляют разницу между соответствующими координатами текущего объекта и объекта obj
    def distance(self, obj):
        dx = self.x - obj.x
        dy = self.y - obj.y
        dz = self.z - obj.z
        # переменная r2 представляет собой квадрат расстояния между объектами в трехмерном пространстве
        r2 = dx ** 2 + dy ** 2 + dz ** 2
        # строка возвращает округленное значение квадратного корня из r2 (фактическое расстояние между объектами)
        return int(math.sqrt(r2))


# LivingObject: это класс, представляющий объект, который может быть живым
class LivingObject(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, hp: int):
        super().__init__(name, loc, x, y, z)
        self._max_hp = hp  # _max_hp (максимальное здоровье) и _hp (текущее здоровье)
        self._hp = hp

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def hp(self):
        return self._hp

    # Проверка, что объект жив, и не позволяет здоровью стать отрицательным или превысить максимальное значение
    def change_hp(self, change):
        if not self.alive:
            return
        self._hp += change
        if self._hp < 0:
            self._hp = 0
        if self._hp > self._max_hp:
            self._hp = self._max_hp

    # alive: Свойство, возвращающее True, если объект жив, и False в противном случае
    @property
    def alive(self):
        return self._hp > 0

    # eat: метод, представляющий попытку объекта съесть другой объект (obj). Если расстояние между объектами меньше 1,
    # вызывается метод eat_me() объекта obj
    def eat(self, obj):
        if self.distance(obj) > 1:
            return
        self.change_hp(obj.eat_me())


# Weapon: Это класс, представляющий оружие, которое может атаковать живые объекты
class Weapon(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        super().__init__(name, loc, x, y, z)
        self._damage = damage
        self._radius = radius

    @property
    def damage(self):
        return self._damage

    @property
    def radius(self):
        return self._radius

    # attack: Метод, представляющий атаку оружия. Если расстояние меньше радиуса атаки, причиняет цели урон,
    # вызывая метод change_hp() объекта obj
    def attack(self, obj: LivingObject):
        d = self.distance(obj)
        if d > self.radius:
            return
        obj.change_hp(-self.damage)


# Eatable: Это абстрактный базовый класс для объектов, которые можно съесть. _hp (количество здоровья, которое объект
# получает при съедении), _eaten (показатель, был ли объект съеден)
class Eatable(ABC):
    def __init__(self, hp: int):
        self._hp = hp
        self._eaten = False

    @property
    def eaten(self):
        return self._eaten

    @abstractmethod
    def eat_me(self):
        if not self.eaten:
            self._eaten = True
            return self._hp
        else:
            return 0


# Food: Это класс для представления объектов-еды
class Food(GameObject, Eatable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eat_me(self):
        Food.eat_me(self)


# Poison: Это класс для представления яда
class Poison(GameObject, Eatable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eat_me(self):
        return -Eatable.eat_me(self)


# Burnable: Это абстрактный базовый класс для объектов, которые можно поджечь. Атрибут _burned
# (показывает, был ли объект подожжен)
class Burnable(ABC):
    def __init__(self):
        self._burned = False

    @property
    def burned(self):
        return self._burned

    @abstractmethod
    def burn_me(self):
        self._burned = True


# Cookable: Это класс для представления объектов, которые можно приготовить. Наследует свойства и методы от трех других
# классов: GameObject, Eatable и Burnable.
class Cookable(GameObject, Eatable, Burnable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)
        Burnable.__init__(self)

    @classmethod
    def grow_mushroom(cls, loc, x, y, z):
        # Создается новый объект класса Cookable с именем 'mushroom', указанным местоположением и координатами, и
        # установленным здоровьем (hp) равным 20
        return cls('mushroom', loc, x, y, z, 20)

    def burn_me(self):
        #  Вызывается метод burn_me из родительского класса Burnable, который показывает горения объекта
        Burnable.burn_me(self)

    def eat_me(self):
        # Вызывается метод eat_me из родительского класса Eatable, который возвращает значение здоровья после
        # съедения объекта.
        hp = Eatable.eat_me(self)
        # Возвращение значения hp (здоровья), когда self.burned равно True, в противном случае возвращается
        # отрицательное значение hp.
        return hp if self.burned else -hp
