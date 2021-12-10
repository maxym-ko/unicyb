class Clock12:
    """
    Class for modeling 12-hours clock dial. Final version.
    The time can be from 00:00 till (max_hour()-1):(max_minute()-1).
    On any try to obtain incorrect value an exception is raised.
    """

    __limit = 100
    __clock_count = 0

    def __init__(self, *args):
        """
        :param args: can accept hours and minutes, or minutes, or other clock
        By default set time to 00:00.
        """

        Clock12._check_limit()

        self.__h = 0
        self.__m = 0
        if len(args) == 0:
            return
        elif len(args) > 2:
            raise TypeError('Clock12.__init__ can not take more than 2 positional arguments.')
        elif len(args) == 2:
            self.set_time(args[0], args[1])
        else:
            if isinstance(args[0], int):
                self._from_int(args[0])
            elif isinstance(args[0], Clock12):
                self._assign(args[0])
            else:
                raise ValueError('The single argument of Clock12.__init__ should be int or Clock12')

        Clock12.__clock_count += 1

    @staticmethod
    def _check_limit():
        if Clock12.__clock_count > Clock12.__limit:
            raise TypeError('You have already created 100 clocks. You cannot create more')

    def get_hour(self):
        return self.__h

    def get_minute(self):
        return self.__m

    def copy(self):
        """Shallow copy."""

        return self.__class__(self)

    def set_time(self, h: int, m: int):
        """
        :param h: correct hours
        :param m: correct minutes
        :return: None
        On incorrect time set nothing and raise en exception.
        """

        self._is_good_time(h, m)
        self._set_time(h, m)

    def _is_good_time(self, h: int, m: int):
        return self._is_good_hour(h) and self._is_good_minute(m)

    def _set_time(self, h: int, m: int):
        self.__h = h
        self.__m = m

    def _is_good_hour(self, h: int):
        if not isinstance(h, int):
            raise TypeError(str(type(h)) + ' is improper for hour value')
        if 0 <= h < self.max_hour():
            return True
        raise ValueError(str(h) + ' is improper for hour value')

    def _is_good_minute(self, m: int):
        if not isinstance(m, int):
            raise TypeError(str(type(m)) + ' is improper for minute value')
        if 0 <= m < self.max_minute():
            return True
        raise ValueError(str(m) + ' is improper for minute value')

    def _assign(self, other):
        self.__h = other.__h
        self.__m = other.__m

    def _from_int(self, minute: int):
        minute %= self.max_hour() * self.max_minute()
        self.__h, self.__m = divmod(minute, self.max_minute())

    def input(self):
        h0 = int(input("Enter hour (0..{}): ".format(self.max_hour() - 1)))
        m0 = int(input("Enter minute (0..{}): ".format(self.max_minute() - 1)))
        self.set_time(h0, m0)

    def __eq__(self, other):
        return self.get_hour() == other.get_hour() and self.get_minute() == other.get_minute()

    def __lt__(self, other):
        return self.get_hour() < other.get_hour() or \
               self.get_hour() == other.get_hour() and self.get_minute() < other.get_minute()

    def __le__(self, other):
        return self < other or self == other

    def __int__(self):
        return self.get_hour() * self.max_minute() + self.get_minute()

    def __add__(self, other):
        tmp = self.copy()
        return tmp.__iadd__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, Clock12):
            return self._iadd_Clock(other)
        elif isinstance(other, int):
            return self._iadd_int(other)
        else:
            return NotImplemented

    # noinspection PyPep8Naming
    def _iadd_Clock(self, other):
        self.__h += other.__h
        self.__m += other.__m
        if self.__m >= self.max_minute():
            self.__h += 1
        self.__m -= self.max_minute()
        if self.__h >= self.max_hour():
            self.__h -= self.max_hour()
        return self

    def _iadd_int(self, minute):
        c = Clock12(minute)
        return self._iadd_Clock(c)

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.get_hour()) + ', ' + str(self.get_minute()) + ')'

    def __str__(self):
        return 'h=' + str(self.get_hour()) + ', m=' + str(self.get_minute())

    def __format__(self, format_spec):
        if format_spec == 'hh:mm':
            fs = '{0:02d}:{1:02d}'
        elif format_spec == 'h:mm':
            fs = '{0:d}:{1:02d}'
        else:
            return self.__str__()
        return fs.format(self.get_hour(), self.get_minute())

    __max_minute = 60
    __max_hour = 12

    @staticmethod
    def max_minute():
        return Clock12.__max_minute

    @staticmethod
    def max_hour():
        return Clock12.__max_hour

    @classmethod
    def first_pair(cls):
        return cls(8, 40)
