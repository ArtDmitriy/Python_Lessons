# Урок 10. Объектно-ориентированное программирование. Продвинутый уровень.


# Задание №1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.


class Matrix:
    """ Matrix """
    __data: dict

    def __init__(self, *elems, rows=1) -> None:

        # test split elems

        self.__data = {}

        if len(elems) % rows != 0:
            raise ValueError("Can't split len(elems) / rows")

        columns = len(elems) // rows

        if len(elems) > 0:
            self.__data["size"] = (rows, columns)

        for column in range(rows):
            for row in range(columns):
                self.__data[(row, column)] = elems[column + row * rows]

    def get_size(self) -> tuple:
        """ return size of matrix (rows, columns) """
        return self.__data.get("size", (0, 0))

    def get_elem(self, row_index, column_index):
        """ return elems of pos(row, column) """

        value = self.__data[(row_index, column_index)]

        if value is not None:
            return value

        raise ValueError(f"Unknow index {(row_index, column_index)}")

    def __arifm_func(self, func, other: 'Matrix') -> list:

        (rows, columns) = self.get_size()

        return [func(self.get_elem(x, y),  other.get_elem(x, y))
                for y in range(rows) for x in range(columns)]

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """ operator + for matrix. return a new matrix """
        if self.get_size() != other.get_size():
            raise ValueError("Matrix's sizies must be eq")

        return Matrix(self.__arifm_func(lambda x, y: x + y, other), rows=self.get_size()[0])

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """ operator - for matrix. return a new matrix """

        if self.get_size() != other.get_size():
            raise ValueError("Matrix's sizies must be eq")

        return Matrix(self.__arifm_func(lambda x, y: x - y, other), rows=self.get_size()[0])

    def __str__(self) -> str:

        (rows, columns) = self.get_size()

        if rows * columns == 0:
            return "Empty Matrix"

        output = ""
        for j, row in enumerate(range(rows)):

            for i, column in enumerate(range(columns)):
                output += f"{self.get_elem(column, row)}"

                if i != columns - 1:
                    output += " "

            if j != rows - 1:
                output += "\n"

        return output



# Задание №2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.



from abc import ABC, abstractmethod


class MaterialLenSolver:
    __length: float = 0
    __coat_list = []
    __costume_list = []

    @property
    def length(self):
        return self.__length

    @property
    def node_list(self):
        return {"coats": self.__coat_list, "costumies": self.__costume_list}

    @node_list.setter
    def node_list(self, other, add=True):
        if other.__class__ is Coat:
            if add:
                self.__coat_list.append(other.get_name())
            else:
                self.__coat_list.remove(other.get_name())
        elif other.__class__ is Costume:
            if add:
                self.__costume_list.append(other.get_name())
            else:
                self.__costume_list.remove(other.get_name())
        else:
            raise ValueError("Unknow cloth  type")

    @length.setter
    def length(self, in_len: float):
        self.__length += in_len

    def __iadd__(self, other):
        self.length = other.material_length()
        self.node_list = other
        return self

    def __isub__(self, other):
        self.length = - other.material_length()
        if other.__class__ is Coat and other.get_name() in self.__costume_list:
            self.__costume_list.remove(other.get_name())
        elif other.__class__ is Costume and other.get_name() in self.__coat_list:
            self.__coat_list.remove(other.get_name())
        return self


class ACloth(ABC):
    name: str

    def get_name(self):
        return self.name

    @abstractmethod
    def material_length(self):
        """ return length of material """


class Coat(ACloth):

    def __init__(self, name, size) -> None:
        super().__init__()
        self.name = name
        self.size = size

    def material_length(self):
        return self.size * 6.5 + 0.5


class Costume(ACloth):

    def __init__(self, name, height) -> None:
        super().__init__()
        self.name = name
        self.height = height

    def material_length(self):
        return 2 * self.height + 0.3


if __name__ == "__main__":

    mtr_solver = MaterialLenSolver()

    mtr_solver += Coat("For user 001", 10)
    mtr_solver += Costume("For film 01", 121)
    mtr_solver += Costume("For film 02", 119)
    mtr_solver += Costume("For film 03", 97)
    mtr_solver += Costume("For film 03", 130)
    mtr_solver += Costume("For film 04", 180)
    mtr_solver += Costume("For film 05", 103)
    mtr_solver += Coat("For user 111", 15)
    mtr_solver += Coat("For user 101", 19)
    mtr_solver += Coat("For user 011", 12)

    print(f"{mtr_solver.length} meters for {mtr_solver.node_list}")


# Задание №3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__, __truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и округление до целого числа деления клеток, соответственно.
# Сложение.
# Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание.
# Участвуют две клетки. Операцию необходимо выполнять,
# только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение.
# Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление.
# Создаётся общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
# В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.
# Подсказка:
# подробный список операторов для перегрузки доступен по ссылке.



class Cell:
    __cells: int

    def __init__(self, cells: int) -> None:
        self.__cells = cells

    def __add__(self, other: 'Cell'):
        return Cell(self._get_size() + other._get_size())

    def __sub__(self, other: 'Cell'):
        if self._get_size() < other._get_size():
            raise ValueError("cells can't be < 0")

        return Cell(self._get_size() - other._get_size())

    def __mul__(self, other: 'Cell'):
        return Cell(self._get_size() * other._get_size())

    def __floordiv__(self, other: 'Cell'):
        return Cell(self._get_size() // other._get_size())

    def _get_cells(self) -> str:
        return str(self).replace("Cell(", "").replace(")", "")

    def _get_size(self) -> int:
        return self._get_cells().count("*")

    def __str__(self) -> str:
        return f"Cell({'*'*self.__cells})"

    def make_order(self, split_cell) -> str:
        """ ordering cells to cube the size eq split_cell*split_cell """

        if split_cell == 0:
            raise ValueError("can't split cells by 0")

        if split_cell >= self._get_size():
            return self._get_cells()

        size = self._get_size()

        return "".join([f"{x}\n" if i % split_cell == 0 and i != size else x
                        for i, x in enumerate(self._get_cells(), start=1)])

