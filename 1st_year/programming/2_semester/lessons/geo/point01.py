from geo.point import Point


class Point01(Point):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._check()

    def _check(self):
        if not (0.0 <= self.x <= 1.0 and 0.0 <= self.y <= 1.0):
            raise ValueError
