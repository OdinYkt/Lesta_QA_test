from .Drawing import Drawing


class Canvas:
    """Холст для рисования"""
    def __init__(self):
        self.figures: list[Drawing] = []

    def add_item(self, item: Drawing):
        """Добавить объект"""
        self.figures.append(item)

    def add_items(self, *items: Drawing):
        """Добавить объекты"""
        for item in items:
            self.add_item(item)

    def draw(self, color=None):
        """Нарисовать все объекты"""

        print(f'Drawing {len(self.figures)} items')
        for figure in self.figures:
            if color:
                print(f'With color: {color} - ', end='')
            figure.draw()

    def clear(self):
        self.figures = []
        print('Canvas cleared\n')


class Engine2D:
    """Движок для 'рисования' на холсте"""
    def __init__(self):
        self.canvas = Canvas()
        self.color = None

    def draw(self):
        self.canvas.draw(color=self.color)
        self.canvas.clear()

    def set_color(self, color: str):
        self.color = color
