# Урок 9. Объектно-ориентированное программирование (ООП).


# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.



import time
import enum


class Colour(enum.Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2


class TrafficLight:
    __colour: Colour
    __move: int = 1

    def __init__(self, colour: Colour) -> None:
        self.__colour = colour

    def running(self, green_t=7, red_t=7, yellow_t=2):

        for _ in range(10):  # while True:
            if self.__colour == Colour.RED:
                print(self.__colour.name)
                time.sleep(red_t)
            elif self.__colour == Colour.YELLOW:
                print(self.__colour.name)
                time.sleep(yellow_t)
            elif self.__colour == Colour.GREEN:
                print(self.__colour.name)
                time.sleep(green_t)

            if self.__colour.value == 2:
                self.__move = -1
            elif self.__colour.value == 0:
                self.__move = 1

            self.__colour = Colour(self.__colour.value + self.__move)


if __name__ == "__main__":
    traffic = TrafficLight(Colour.GREEN)
    traffic.running()



# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:

    _length: float
    _width: float

    def __init__(self, length: float = 0, width: float = 0) -> None:
        self._length = length
        self._width = width

    def calc(self, density: float, thickness: float) -> float:
        return self._length * self._width * density * thickness


if __name__ == "__main__":
    road = Road(length=20, width=5000)
    print(road.calc(25, 5))

    # or if we in module
    road = Road()
    road._length = 20
    road._width = 5000
    print(road.calc(density=25, thickness=5))



# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.



class Worker:
    name: str
    surname: str
    position: str
    _income: dict = {"wage": 0.0, "bonus": 1.0}

    def __init__(self, name: str, surname: str, position: str, income: dict = {"wage": 0, "bonus": 1.0}) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, income: dict = {"wage": 0, "bonus": 1.0}) -> None:
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income["wage"] * self._income["bonus"]


if __name__ == "__main__":
    position = Position("Alex", "Zhem", "Programmer",
                            {"wage": 100, "bonus": 1.5})

    position.name = "Alexandr"
    position.position += "|MedTech"

    position._income["bonus"] = 1.0

    print(position.get_full_name.__name__, position.get_full_name())
    print(position.position)
    print(position.get_total_income.__name__, position.get_total_income())



# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.



from enum import Enum


class TURN(Enum):
    LEFT = 0
    RIGHT = 1


class Car:
    speed: float
    _colour: str  # or use colour lib
    _name: str
    _is_police: bool = False

    def __init__(self, colour, name) -> None:
        self._colour = colour
        self._name = name

    def go(self) -> None:
        print(f"{self._name} is start")

    def stop(self) -> None:
        print(f"{self._name} is stop")

    def turn(self, turn_side: TURN) -> None:
        print(f"{self._name} is turn to {turn_side.name}")

    def show_speed(self) -> float:
        return self.speed


class TownCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)

    def show_speed(self) -> float:

        spd = super().show_speed()

        if spd > 40:
            print("Overspeed (40)")

        return spd


class SportCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)


class WorkCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)

    def show_speed(self) -> float:
        spd = super().show_speed()

        if spd > 60:
            print("Overspeed (60)")

        return spd


class PoliceCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)
        self._is_police = True


if __name__ == "__main__":
    abstract_car = Car("Transparent", "SomeCar")
    town_car = TownCar("Black", "TownCar")
    work_car = WorkCar("Green", "WorkCar")
    police_car = PoliceCar("DarkBlue", "PoliceCar")

    abstract_car.speed = -100 # =)
    town_car.speed = 120
    work_car.speed = 160
    police_car.speed = 175

    for some in [abstract_car, town_car, work_car, police_car]:
        print(f"{some.__class__}._name = {some._name}")
        print(f"{some.__class__}._colour = {some._colour}")
        print(f"{some.__class__}._is_police = {some._is_police}")

        print(f"{some.__class__}.go() => ", end="")
        some.go()

        print(f"{some.__class__}.stop() => ", end="")
        some.stop()

        print(f"{some.__class__}.turn(TURN.RIGHT) => ", end="")
        some.turn(TURN.RIGHT)

        print(f"{some.__class__}.turn(TURN.LEFT) => ", end="")
        some.turn(TURN.LEFT)

        print(f"{some.__class__}.show_speed() => {some.show_speed()}", end="\n\n")


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.



class Stationery:
    title: str

    def draw(self) -> None:
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "ручка"

    def draw(self) -> None:
        print("Пишем текст")
        return None


class Pencil(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "карандаш"

    def draw(self) -> None:
        print("Чертим чертеж")
        return None


class Handle(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "маркер"

    def draw(self) -> None:
        print("Выделяем заголовки")
        return None


if __name__ == "__main__":
    pen = Pen()
    pencil = Pencil()
    handle = Handle()

    for some in [pen, pencil, handle]:
        print(f"{some.__class__}:title = {some.title}")
        print(f"{some.__class__}.draw() =>\t", end="")
        some.draw()
        print()