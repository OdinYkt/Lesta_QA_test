from abc import ABC, abstractmethod
from typing import Union

from .Point import Point
from .utils.NumberDescriptor import PositiveNumber


class Drawing(ABC):
    """
    Абстрактный класс для объектов, которые могут быть отрисованы
    """
    draw_text = ""

    @abstractmethod
    def draw(self):
        pass


class Square(Drawing):
    """
    Квадрат
        - center_p - центр квадрата
        - vertex - вершины
        - draw() - отрисовать квадрат

    Для отрисовки точки выводятся с левой нижней по часовой стрелке
    """
    draw_text = 'Drawing Square: center - {center_p}; vertex - {vertex}'
    size = PositiveNumber()

    def __init__(self, bottom_left_p: Union[Point, tuple], size: Union[int, float]):
        """
        Задаются нижняя левая точка квадрата и размер стороны

        :param bottom_left_p: Координаты нижней левой точки или точка на плоскости
        :param size: Размер стороны, положительное число
        """
        super(Square, self).__init__()
        self.bottom_left_p = Point(bottom_left_p)
        self.size = size

    @property
    def vertex(self):
        """Вершины"""
        x, y = self.bottom_left_p.x, self.bottom_left_p.y

        top_left = (x, y + self.size)
        top_right = (x + self.size, y + self.size)
        bottom_right = (x + self.size, y)

        return self.bottom_left_p, Point(*top_left), Point(*top_right), Point(*bottom_right)

    @property
    def center_p(self):
        """Центр квадрата"""
        half_size = self.size / 2
        return Point(self.bottom_left_p.x + half_size, self.bottom_left_p.y + half_size)

    def draw(self):
        print(self.draw_text.format(
            center_p=self.center_p,
            vertex=self.vertex)
        )


class Triangle(Drawing):
    """
    Треугольник
        - vertex - вершины треугольника
        - center_p - центр треугольника
        - draw() - отрисовать треугольник
    """
    draw_text = 'Drawing Triangle: center - {center_p}; vertex - {vertex}'

    def __init__(self, p1: Union[Point, tuple], p2: Union[Point, tuple], p3: Union[Point, tuple]):
        """
        Задаются вершины треугольника

        :param p1: Координаты точки или точка на плоскости
        :param p2: Координаты точки или точка на плоскости
        :param p3: Координаты точки или точка на плоскости
        """
        super(Triangle, self).__init__()
        self.vertex: tuple[Point, ...] = (Point(p1), Point(p2), Point(p3))

    @property
    def center_p(self):
        return Point(
            x=sum([p.x for p in self.vertex]) / 3,
            y=sum([p.y for p in self.vertex]) / 3,
        )

    def draw(self):
        print(self.draw_text.format(
            center_p=self.center_p,
            vertex=self.vertex,
        ))


class Circle(Drawing):
    """
    Круг
        - center_p - центр круга
        - radius - радиус круга
        - draw() - отрисовать круг
    """
    draw_text = 'Drawing Circle: center - {center_p}; radius - {radius}'
    radius = PositiveNumber()

    def __init__(self, center_p: Union[Point, tuple], radius: Union[int, float]):
        """
        Задаются центр и радиус

        :param center_p: Координаты точки или точка на плоскости
        :param radius: Радиус, положительное число
        """
        self.center_p = Point(center_p)
        self.radius = radius

    def draw(self):
        print(self.draw_text.format(
            center_p=self.center_p,
            radius=self.radius,
        ))
