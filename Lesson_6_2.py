class Road:
    # конструктор
    def __init__(self, length, width):
        self._length = length  # атрибуты класса (объявляются вне метода)
        self._width = width  # атрибуты класса (объявляются вне метода)

    def get_full_profit(self, weight=35, thickness=10):
        # атрибуты объекта (экземпляра) объявляются внутри метода
        return f"{self._length} м * {self._width} м * {weight} кг * {thickness} см =" \
               f" {(self._length * self._width * weight * thickness) / 1000} т"
                # получение доступа к атрибутам объекта через self


road_1 = Road(40000, 40)  # передача значений атрибутам класса
print(road_1.get_full_profit())