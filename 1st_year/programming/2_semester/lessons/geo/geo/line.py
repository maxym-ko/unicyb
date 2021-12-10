import math

from common.comparator import Comparator
from common.numeric import num2float as conversion
from geo.point import Point


class Line:
    """ Line on the plane.

    Interface provides immutable copyable object.

    At present line implementation uses equation ax+by+c=0 with normalized coefficients.
    All comparisons on == and ==0 in method's implementation are done with some accuracy.
    Comparator object is used.
    """
    _cmp = Comparator()

    @classmethod
    def cmp(cls):
        """Return Comparator object to check == and ==0"""
        return cls._cmp

    def __init__(self, *args):
        """

        :param args: line can be set
                        by numeric a,b,c from ax+by+c=0
                        by points A,B (of type Point)
                        by other line (of type Line)
        """
        self._init()
        if len(args) > 3:
            raise TypeError('Too much arguments to construct Line.')
        elif len(args) == 3:
            self._init_from_abc(*args)
        elif len(args) == 2:
            self._init_from_points(*args)
        elif len(args) == 1:
            if isinstance(args[0], Line):
                self._assign(args[0])
            elif hasattr(args[0], 'to_line'):
                self._assign(args[0].to_line())
            else:
                raise TypeError('Unable convert ' + args[0].__class__.__name__ + ' to Line')

    def _init(self):
        self._a = 0.0
        self._b = 0.0
        self._c = 0.0
        self._state = False
        self._normalize()

    def _assign(self, other):
        """
         :param other: Line, no checks
        """
        self._a = other._a
        self._b = other._b
        self._c = other._c
        self._state = other._state
        # self._normalize()

    def _init_from_points(self, a: Point, b: Point):
        if not (isinstance(a, Point) and isinstance(b, Point)):
            raise TypeError('Improper types ' + a.__class__.__name__ + ', '
                            + b.__class__.__name__ + ' to construct Line by Points')
        dx = b.x - a.x
        dy = b.y - a.y
        self._set(dy, -dx, dx * a.y - dy * a.x)

    def _init_from_abc(self, a, b, c):
        a = conversion(a)
        b = conversion(b)
        c = conversion(c)
        self._set(a, b, c)

    def _set(self, a, b, c):
        if not (math.isfinite(a) and math.isfinite(b) and math.isfinite(c)):
            self._init()
            return
        self._a = a
        self._b = b
        self._c = c
        self._normalize()

    def _normalize(self):
        if self._b:
            self._a /= self._b
            self._c /= self._b
            self._b = 1.0
        elif self._a:
            self._c /= self._a
            self._a = 1.0
        else:
            self._c = 0.0
        self._check()

    def _check(self):
        self._state = self._a or self._b

    def __bool__(self):
        return bool(self._state)

    def __eq__(self, other):
        """
        Check == for lines with some accuracy.
        Invalid lines is equal.
        """
        # code is simplified due to normal form and invalid lines equality
        return (self._cmp.isequal(self._a, other._a)
                and self._cmp.isequal(self._b, other._b)
                and self._cmp.isequal(self._c, other._c))

    def __contains__(self, item: Point):
        if isinstance(item, Point):
            return self and self._cmp.iszero(self.distance_signed_y(item))
        else:
            return False

    def collinear(self, other):
        if not self:
            return False
        elif isinstance(other, Line):
            return other and self._cmp.isequal(self._a, other._a) and self._cmp.isequal(self._b, other._b)
        elif hasattr(other, 'collinear'):
            return other.collinear(self)
        else:
            return False

    def parallel(self, other):
        if isinstance(other, Line):
            return self.collinear(other) and self != other
        elif hasattr(other, 'parallel'):
            return other.parallel(self)
        else:
            return False

    def perpendicular(self, other):
        if not self:
            return False
        elif isinstance(other, Line):
            return other and self._cmp.iszero(self._a * other._a + self._b * other._b)
        elif hasattr(other, 'perpendicular'):
            return other.perpendicular(self)
        else:
            return False

    def intersecting(self, other):
        if not self:
            return False
        elif isinstance(other, Line):
            return other and not self.collinear(other)
        elif hasattr(other, 'intersecting'):
            return other.intersecting(self)
        else:
            return False

    def intersection(self, other):
        if not self:
            raise ValueError()
        elif isinstance(other, Line):
            if not self.intersecting(other):
                raise ValueError()
            det = self._a * other._b - other._a * self._b
            return Point(- (self._c * other._b - other._c * self._b) / det,
                         - (self._a * other._c - other._a * self._c) / det)
        elif hasattr(other, 'intersection'):
            return other.intersection(self)
        else:
            raise NotImplementedError

    def distance_signed_y(self, p: Point) -> float:
        if not self:
            return math.nan
        return self._a * p.x + self._b * p.y + self._c

    def distance_signed(self, p: Point) -> float:
        d = self.distance_signed_y(p)
        if not self:
            return d
        return d / math.hypot(self._a, self._b)

    def other_side(self, p1: Point, p2: Point):
        if not self:
            return False
        d1 = self.distance_signed_y(p1)
        d2 = self.distance_signed_y(p2)
        return (d1 < 0 and d2 > 0) or (d1 > 0 and d2 < 0)

    def one_side(self, p1: Point, p2: Point):
        if not self:
            return False
        d1 = self.distance_signed_y(p1)
        d2 = self.distance_signed_y(p2)
        return (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)

    def __repr__(self):
        return f"{self._a}*x {self._b:+}*y {self._c:+}" + str(bool(self))

    def __sub__(self, other):
        if not self:
            return math.nan
        if isinstance(other, Point):
            return abs(self.distance_signed(other))
        elif isinstance(other, Line):
            if not self.collinear(other):
                return math.nan
            else:
                return abs(self._c - other._c) / math.hypot(self._a, self._b)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Point):
            return self.__sub__(other)
        else:
            raise NotImplementedError

    def copy(self):
        return self.__class__(self)
