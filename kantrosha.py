class Shape:

    def __init__(self):
        self._pos = []
        self._sca = 0
        self._col = ''

    def set_pos(self, x, y):
        self._pos = [x, y]

    def set_sca(self, scale):
        self._sca = scale

    def set_col(self, color):
        self._col = color

    def get_pos(self):
        return self._pos

    def get_sca(self):
        return self._pos

    def get_col(self):
        return self._col

    def info(self):
        print(f'Координаты - {self._pos}, масштаб - {self._sca}, цвет - {self._col}')

    def area(self):
        print(f'Площадь фигуры ', end='')


class Rectangle(Shape):

    def __init__(self):
        super().__init__()
        self._side1 = 0
        self._side2 = 0

    def set_sides(self, s1, s2):
        self._side1 = s1
        self._side2 = s2

    def get_sides(self):
        return self._side1
        return self._side2

    def info(self):
        super().info()
        print(f'Сторона a = {self._side1}, сторона b = {self._side2}')

    def area(self):
        super().area()
        print(f'{self._side1 * self._side2}')


class Trapezoid(Shape):

    def __init__(self):
        super().__init__()
        self._side1 = 0
        self._side2 = 0
        self._h = 0

    def set_sides(self, s1, s2, h):
        self._side1 = s1
        self._side2 = s2
        self._h = h

    def get_sides(self):
        return self._side1
        return self._side2
        return self._h

    def info(self):
        super().info()
        print(f'Сторона a = {self._side1}, сторона b = {self._side2}, высота = {self._h}')

    def area(self):
        super().area()
        print(f'{((self._side1 + self._side2) / 2) * self._h}')


class Circle(Shape):

    def __init__(self):
        super().__init__()
        self._radius = 0

    def set_radius(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def info(self):
        super().info()
        print(f'Радиус = {self._radius}')

    def area(self):
        super().area()
        print(f'{3.14 * self._radius ** 2}')


rec = Rectangle()
rec.set_sides(10, 5)
rec.set_pos(10, 10)
rec.set_sca(100)
rec.set_col('green')
rec.info()
rec.area()

tra = Trapezoid()
tra.set_sides(20, 10, 5)
tra.set_pos(2, 10)
tra.set_sca(50)
tra.set_col('red')
tra.info()
tra.area()

cir = Circle()
cir.set_radius(20)
cir.set_pos(20, 30)
cir.set_sca(30)
cir.set_col('blue')
cir.info()
cir.area()
print ("Всё ок")
