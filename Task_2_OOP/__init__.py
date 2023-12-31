"""
Содержит классы для "рисования" фигур на холсте с помощью движка Engine2D

Полный текст задания в __task__

Пример использования в example.py
Юнит тесты в tests

Реализация создания фигур основана на простейших способах задания произвольных фигур соответствующего вида.
    - Квадрат через одну из точек и размер стороны (по аналогии создания прямоугольников в PyQt)
    - Треугольник через координаты всех вершин
    - Окружность через центр и радиус

Очевидно, если требуется более сложное создание или поведение фигур на холсте
(треугольник через две линии и угол, поворот фигур, поиск пересечений, трансформация),
рекомендуется ввести класс векторов, а также сделать фигуры состоящими из соответствующих прямых
"""

from .Engine import Engine2D

from .Point import Point
from .Drawing import Circle, Triangle, Square

from .example import example, example_color
