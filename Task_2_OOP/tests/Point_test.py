import pytest
from pytest import approx
from ..Point import Point


def test_str_representation():
    p = Point(1, 2)
    assert str(p) == '({:.2f}, {:.2f})'.format(p.x, p.y)


def test_incorrect_args():
    with pytest.raises(ValueError):
        Point(1, 2, 3)
    with pytest.raises(ValueError):
        Point(1)
    with pytest.raises(ValueError):
        Point((1, 2, 3))
    with pytest.raises(ValueError):
        Point('1', '2')
    with pytest.raises(ValueError):
        Point((1,), 2)


def test_from_point():
    p1 = Point(1, 2)
    p2 = Point(p1)
    assert p1.x == approx(p2.x)
    assert p1.y == approx(p2.y)


def test_from_tuple():
    xy = (1, 2)
    p = Point(xy)
    assert p.x == approx(xy[0])
    assert p.y == approx(xy[1])


def test_from_xy():
    x, y = 1, 2
    p = Point(x, y)
    assert p.x == approx(x)
    assert p.y == approx(y)
