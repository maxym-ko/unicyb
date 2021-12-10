import math


class Point:

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __init__(self, *args):
        self._x = 0
        self._y = 0
        if len(args) == 2:
            self._init_from_xy(*args)
        elif len(args) == 0:
            return
        elif len(args) == 1:
            self._init_from_Point(*args)
        else:
            raise ValueError('Wrong arguments')

    def _init_from_xy(self, x, y):
        x = self._convert(x)
        y = self._convert(y)
        self._set_xy(x, y)

    def _init_from_Point(self, point):
        if isinstance(point, Point):
            self._set_xy(point.x, point.y)
        else:
            raise ValueError("Wrong arguments")

    def _set_xy(self, x, y):
        self._x = x
        self._y = y

    @staticmethod
    def _convert(x):
        if isinstance(x, int):
            return float(x)
        elif isinstance(x, float):
            if math.isfinite(x):
                return x
            else:
                raise ValueError('x should be finite')
        raise TypeError('x should be int or float')

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
