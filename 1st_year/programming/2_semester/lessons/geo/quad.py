# Дописати
from geo.line import Line
from geo.point import Point


class Quad:

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @property
    def d(self):
        return self._d

    def __init__(self, a, b, c, d):
        if not (isinstance(a, Point) and isinstance(b, Point) and isinstance(c, Point) and isinstance(d, Point)):
            raise TypeError("a, b, c, d should be Points")
        self._a = self._b = self._c = self._d = Point(0, 0)
        self._OK = False
        self._set(a, b, c, d)
        self._check()

    def _set(self, a, b, c, d):
        pass

    def _check(self):
        tmp = {self.a, self.b, self.c, self.d}
        self._OK = len(tmp) == 4

    def _set(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def is_trapezoid(self):
        if not self:
            return False
        ab = Line(self.a, self.b)
        bc = Line(self.b, self.c)
        cd = Line(self.c, self.d)
        da = Line(self.d, self.a)
        return ab.parallel(cd) and not bc.collinear(da)

    def __bool__(self):
        pass

    def __repr__(self):
        pass
