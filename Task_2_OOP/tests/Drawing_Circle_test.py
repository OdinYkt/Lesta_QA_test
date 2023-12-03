from ..Point import Point
from ..Drawing import Circle

import pytest


@pytest.fixture
def circle():
    center_p = Point(0, 0)
    radius = 5
    return Circle(center_p, radius)


def test_negative_radius(circle):
    with pytest.raises(ValueError):
        Circle(Point(0, 0), -5)


def test_draw(circle, capsys):
    circle.draw()

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert that the expected message is in the captured output
    assert captured.out == f'Drawing Circle: center - {circle.center_p}; radius - {circle.radius}\n'
    assert captured.err == ''
