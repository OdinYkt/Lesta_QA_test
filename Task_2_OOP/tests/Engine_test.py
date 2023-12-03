from ..Drawing import Circle, Triangle, Square
from ..Engine import Engine2D


def test_empty_draw(capsys):
    expected = 'Drawing 0 items\nCanvas cleared'
    engine = Engine2D()
    engine.draw()

    captured = capsys.readouterr()
    assert captured.out.strip() == expected


def test_draw(capsys):
    expected = """Drawing 3 items
Drawing Square: center - (5.25, 5.25); vertex - ((0.25, 0.25), (0.25, 10.25), (10.25, 10.25), (10.25, 0.25))
Drawing Triangle: center - (13.67, 17.00); vertex - ((10.00, 10.00), (11.00, 20.00), (20.00, 21.00))
Drawing Circle: center - (-10.00, -10.00); radius - 10
Canvas cleared

"""

    engine = Engine2D()

    # Создание объектов
    square = Square((0.25, 0.25), size=10)
    triangle = Triangle((10, 10), (11, 20), (20, 21))
    circle = Circle((-10, -10), radius=10)

    engine.canvas.add_items(square, triangle, circle)

    engine.draw()

    captured = capsys.readouterr()

    assert captured.out == expected


def test_color_draw(capsys):
    expected = """Drawing 3 items
With color: green - Drawing Square: center - (5.25, 5.25); vertex - ((0.25, 0.25), (0.25, 10.25), (10.25, 10.25), (10.25, 0.25))
With color: green - Drawing Triangle: center - (13.67, 17.00); vertex - ((10.00, 10.00), (11.00, 20.00), (20.00, 21.00))
With color: green - Drawing Circle: center - (-10.00, -10.00); radius - 10
Canvas cleared

"""

    engine = Engine2D()

    # Создание объектов
    square = Square((0.25, 0.25), size=10)
    triangle = Triangle((10, 10), (11, 20), (20, 21))
    circle = Circle((-10, -10), radius=10)

    engine.canvas.add_items(square, triangle, circle)
    engine.set_color('green')

    engine.draw()

    captured = capsys.readouterr()

    assert captured.out == expected


def test_clear_after_draw(capsys):
    expected_first = """Drawing 3 items
Drawing Square: center - (5.25, 5.25); vertex - ((0.25, 0.25), (0.25, 10.25), (10.25, 10.25), (10.25, 0.25))
Drawing Triangle: center - (13.67, 17.00); vertex - ((10.00, 10.00), (11.00, 20.00), (20.00, 21.00))
Drawing Circle: center - (-10.00, -10.00); radius - 10
Canvas cleared

"""

    expected_second = 'Drawing 0 items\nCanvas cleared\n\n'

    engine = Engine2D()

    # Создание объектов
    square = Square((0.25, 0.25), size=10)
    triangle = Triangle((10, 10), (11, 20), (20, 21))
    circle = Circle((-10, -10), radius=10)

    engine.canvas.add_items(square, triangle, circle)

    engine.draw()

    engine.draw()

    captured = capsys.readouterr()

    assert captured.out == expected_first + expected_second


def test_color_after_draw(capsys):
    expected_first = """Drawing 3 items
With color: green - Drawing Square: center - (5.25, 5.25); vertex - ((0.25, 0.25), (0.25, 10.25), (10.25, 10.25), (10.25, 0.25))
With color: green - Drawing Triangle: center - (13.67, 17.00); vertex - ((10.00, 10.00), (11.00, 20.00), (20.00, 21.00))
With color: green - Drawing Circle: center - (-10.00, -10.00); radius - 10
Canvas cleared

"""

    expected_second = """Drawing 3 items
With color: green - Drawing Square: center - (5.25, 5.25); vertex - ((0.25, 0.25), (0.25, 10.25), (10.25, 10.25), (10.25, 0.25))
With color: green - Drawing Triangle: center - (13.67, 17.00); vertex - ((10.00, 10.00), (11.00, 20.00), (20.00, 21.00))
With color: green - Drawing Circle: center - (-10.00, -10.00); radius - 10
Canvas cleared

"""

    engine = Engine2D()

    # Создание объектов
    square = Square((0.25, 0.25), size=10)
    triangle = Triangle((10, 10), (11, 20), (20, 21))
    circle = Circle((-10, -10), radius=10)

    engine.canvas.add_items(square, triangle, circle)
    engine.set_color('green')

    engine.draw()

    engine.canvas.add_items(square, triangle, circle)

    engine.draw()

    captured = capsys.readouterr()

    assert captured.out == expected_first + expected_second