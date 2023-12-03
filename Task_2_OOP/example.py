from Task_2_OOP.Engine import Engine2D
from Task_2_OOP.Point import Point
from Task_2_OOP.Drawing import Circle, Square, Triangle


def example():
    """Пример использования без цвета"""

    engine = Engine2D()

    # Создание объектов
    square = Square(
        Point(0.25, 0.25),  # Точку можно задавать через объект точки
        size=10
    )
    triangle = Triangle(
        (10, 10), (11, 20), (20, 21)  # или через кортеж
    )
    circle = Circle(
        Point(-10, -10),
        radius=10
    )

    engine.canvas.add_item(square)
    engine.canvas.add_items(triangle, circle)  # Добавление нескольких объектов

    engine.draw()


def example_color():
    """Пример использования с цветом"""

    engine = Engine2D()

    # Создание объектов
    square = Square(
        Point(0.25, 0.25),  # Точку можно задавать через объект точки
        size=10
    )
    triangle = Triangle(
        (10, 10), (11, 20), (20, 21)  # или через кортеж
    )
    circle = Circle(
        Point(-10, -10),
        radius=10
    )

    engine.canvas.add_items(square, triangle, square, circle)

    engine.set_color('green')

    engine.draw()


if __name__ == '__main__':
    example()

    example_color()