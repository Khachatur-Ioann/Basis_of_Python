from random import choice

class Car:
    """ Main car """
    direction = ["🡡 north", "northeast 🡥", "east 🡢", "southeast 🡦",
                 "south 🡣", "🡧 southwest", "🡠 west", "🡤 northwest"]

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'New car: {n} has a color: {c}.\nIs the car a police car? {p}')

    def go(self):
        print(f'{self.name}: Car went.')

    def stop(self):
        print(f'{self.name}: Сar stopped!')

    def turn(self):
        print(f'{self.name}: Car turned {choice(self.direction)}.')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}.'


class TownCar(Car):
    """ City car """

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    """ Cargo truck """

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """ Sports Car """


class PoliceCar(Car):
    """ Patrol car """

    def __init__(self, n, c, s):
        # создание конструктора после потомков связано с тем,
        # что объектам присваиваются потомки, иначе мы не смогли их присвоить
        super().__init__(n, c, s, p=True)  # передаем значения атрибутам класса родителя

# объявление объектов
police_car = PoliceCar('"Полицайка"', 'белый', 80)
work_car = WorkCar('"Грузовичок"', 'хаки', 40)
sport_car = SportCar('"Спортивка"', 'красный', 120)
town_car = TownCar('"Малютка"', 'жёлтый', 65)

list_of_cars = [police_car, work_car, sport_car, town_car]

# взаимодействие с каждым объектом через обращение к методам в цикле
for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()