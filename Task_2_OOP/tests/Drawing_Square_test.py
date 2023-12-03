from ..Point import Point
from ..Drawing import Square

import pytest
from pytest import approx


@pytest.fixture
def square():
    bottom_left_point = Point(0, 0)
    size = 5
    return Square(bottom_left_point, size)


def test_negative_size():
    with pytest.raises(ValueError):
        Square(Point(0, 0), -5)


def test_vertex(square):
    expected_vertex = (
        square.bottom_left_p,
        Point(square.bottom_left_p.x, square.bottom_left_p.y + square.size),
        Point(square.bottom_left_p.x + square.size, square.bottom_left_p.y + square.size),
        Point(square.bottom_left_p.x + square.size, square.bottom_left_p.y)
    )

    for value, expected in zip(square.vertex, expected_vertex):
        assert value.x == approx(expected.x)
        assert value.y == approx(expected.y)
        assert str(value) == str(expected)


def test_center_p(square):
    expected_center = Point(square.bottom_left_p.x + square.size / 2, square.bottom_left_p.y + square.size / 2)
    assert square.center_p.x == approx(expected_center.x)
    assert square.center_p.y == approx(expected_center.y)
    assert str(square.center_p) == str(expected_center)


def test_draw(square, capsys):
    square.draw()

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert that the expected message is in the captured output
    assert captured.out == f'Drawing Square: center - {square.center_p}; vertex - {square.vertex}\n'
    assert captured.err == ''
