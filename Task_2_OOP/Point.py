from .utils.NumberDescriptor import NumberDescriptor


class Point:
    """
    Точка на плоскости
    """
    x = NumberDescriptor()
    y = NumberDescriptor()

    def __init__(self, *args, **kwargs):
        """
        Point(x: Union[int, float], y: Union[int, float])
        Point(a0: tuple)
        Point(point: Point)
        """
        if len(args) < 1 and len(kwargs) < 1:
            raise ValueError("Can't create empty point")

        if kwargs.get('x') is not None and kwargs.get('y') is not None:
            self.x, self.y = kwargs['x'], kwargs['y']

        elif isinstance(args[0], (tuple, list)):
            self.x, self.y = args[0]

        elif isinstance(args[0], Point):
            self.x, self.y = args[0].x, args[0].y

        elif len(args) == 2:
            self.x, self.y = args

        else:
            raise ValueError("Can't create point")

    def __str__(self):
        return '({:.2f}, {:.2f})'.format(self.x, self.y)

    def __repr__(self):
        return str(self)
