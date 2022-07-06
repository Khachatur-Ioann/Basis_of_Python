from abc import ABC, abstractmethod

class Clothes(ABC):
    result = 0

    # если не будет конструктора, то потомки будет иметь право не взаимодействовать, не передовать родителю
    def __init__(self, param):
        self.param = param

    @property  # чтобы взаимодействовать с методом как с атрибутом
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"

class Coat(Clothes):
    @property  # чтобы взаимодействовать с методом как с атрибутом
    def consumption(self):
        return round(self.param / 6.5) + 0.5  # расход ткани для пальто, здесь возвращает 6,5

class Costume(Clothes):
    @property  # чтобы взаимодействовать с методом как с атрибутом
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)  # расход ткани для костюма, здесь возвращает 3

coat = Coat(42)
costume = Costume(170)
print(coat + costume + coat)