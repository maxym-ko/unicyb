import math

from common.numeric import num2float


class Point:
    """
    2D point, finite float coordinates

    Interface provides immutable hashable copyable object.
    """

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __init__(self, *args, **kwargs):
        """
        default (0.0, 0.0)
        :param args: 2 number (float or int convertible to float) or 1 number (complex)
        :param kwargs: x, y (float or int convertible to float) or r, alpha (both float or int convertible to float)
        """
        self._x = 0.0
        self._y = 0.0
        if len(args) == 0:
            if len(kwargs) > 0:
                self._init_from_kwargs(**kwargs)
        elif len(kwargs) > 0:
            raise TypeError('Point should be construct from positional xor keyword arguments')
        else:
            self._init_from_args(*args)

    def _init_from_kwargs(self, **kwargs):
        if len(kwargs) != 2:
            raise TypeError('Improper number of keyword arguments to construct point.')
        if 'x' in kwargs:
            if 'y' not in kwargs:
                raise TypeError('No "y" keyword argument to construct point.')
            self._init_from_rectangular(kwargs['x'], kwargs['y'])
        elif 'r' in kwargs:
            if 'alpha' not in kwargs:
                raise TypeError('No "alpha" keyword argument to construct point.')
            self._init_from_angular(kwargs['r'], kwargs['alpha'])
        else:
            raise TypeError('Unknown keyword arguments to construct point.')

    def _init_from_args(self, *args):
        """
        pre: args is not empty
        """
        if len(args) > 2:
            raise TypeError('Improper number of arguments to construct point.')
        elif len(args) == 2:
            self._init_from_rectangular(*args)
        elif isinstance(args[0], complex):
            self._init_from_complex(args[0])
        elif isinstance(args[0], Point):
            self._assign(args[0])
        else:
            raise TypeError('Improper argument type to construct point: waiting for complex or Point.')

    def _assign(self, other):
        """
        :param other: Point, no checks
        """
        self._set0(other.x, other.y)

    def _set0(self, x, y):
        self._x = x
        self._y = y

    def _init_from_complex(self, c: complex):
        """
        :param c: should be finite complex, else raise  ValueError
        :return: None
        """
        self._set(c.real, c.imag)

    def _init_from_rectangular(self, x, y):
        """
          :param x,y: should be finite real or convertible to float int, else raise TypeError or ValueError
          :return: None
          """
        x = num2float(x)
        y = num2float(y)
        self._set(x, y)

    def _init_from_angular(self, r, alpha):
        """
          :param r, alpha: should be finite real or convertible to float int, else raise TypeError or ValueError
          :return: None
          """
        r = num2float(r)
        alpha = num2float(alpha)
        x = r * math.cos(alpha)
        y = r * math.sin(alpha)
        self._set(x, y)

    def _set(self, x: float, y: float):
        if not (math.isfinite(x) and math.isfinite(y)):
            raise ValueError('Point couldn\'t be infinite.')
        self._set0(x, y)

    def __eq__(self, other):
        """Compare one point (not its identity) with other."""
        return isinstance(other, Point) and (self.x == other.x and self.y == other.y)

    def __lt__(self, other):
        """Lexicographic comparison."""
        return isinstance(other, Point) and (self.x < other.x or (self.x == other.x and self.y < other.y))

    def __le__(self, other):
        return self == other or self < other

    def __sub__(self, other):
        """Return distance from self to other."""
        if isinstance(other, Point):
            return math.hypot(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def distance2(self, other):
        """Return squared distance from self to other."""
        if isinstance(other, Point):
            dx = self.x - other.x
            dy = self.y - other.y
            return dx * dx + dy * dy
        else:
            raise NotImplementedError

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'

    def __str__(self):
        return f'({self.x!s}, {self.y!s})'

    def __format__(self, format_spec):
        """Format each coordinate with the same specification."""
        return f'({self.x:{format_spec}}, {self.y:{format_spec}})'

    def compare_x(self, other):
        """
        Compare x-coordinates.

        In case <, ==, > return negative, zero or positive value correspondingly.
        """
        return self.x - other.x

    def compare_y(self, other):
        """
        Compare y-coordinates.

        In case <, ==, > return negative, zero or positive value correspondingly.
        """
        return self.y - other.y

    @classmethod
    def input(cls, prompt=''):
        if prompt:
            print(prompt, end='')
        x = float(input('Enter the x-coordinate: '))
        y = float(input('Enter the y-coordinate: '))
        return cls(x, y)

    def copy(self):
        return self.__class__(self)

    def __hash__(self):
        return hash((self.x, self.y))
