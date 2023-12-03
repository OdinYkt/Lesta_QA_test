from ..Point import Point
from ..Drawing import Triangle

import pytest
from pytest import approx


@pytest.fixture
def triangle():
    points = ((0, 0), (0, 5), (5, 0))
    return Triangle(*points)


def test_center_p(triangle):
    expected_center = Point(
        x=sum([point.x for point in triangle.vertex]) / 3,
        y=sum([point.y for point in triangle.vertex]) / 3,
    )

    assert expected_center.x == approx(triangle.center_p.x)
    assert expected_center.y == approx(triangle.center_p.y)
    assert str(triangle.center_p) == str(expected_center)


def test_draw(triangle, capsys):
    triangle.draw()

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert that the expected message is in the captured output
    assert captured.out == f'Drawing Triangle: center - {triangle.center_p}; vertex - {triangle.vertex}\n'
    assert captured.err == ''
