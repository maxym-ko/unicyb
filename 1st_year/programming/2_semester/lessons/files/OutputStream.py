# 22_13
class FloatInputStream:
    _LEN = 1024

    def __init__(self, path):
        self._f = open(path)
        self._buf = ''
        self._cur = 0
        self._parts = []
        self._eof = False

    def read(self):
        if (parts := self._read_first_part()) == 0:
            return None
        while parts > 1:
            parts = self._get_next_part()
        s = ''.join(self._parts)
        self._parts.clear()
        return float(s)

    def _read_first_part(self):
        if not self._move_to_not_space():
            return 0
        pos1 = self._cur
        parts = 1 + (not self._set_on_first_space())
        pos2 = self._cur
        self._parts.append(self._buf[pos1: pos2])
        return parts

    def _set_on_first_space(self):
        while self._cur < len(self._buf) and not (self._buf[self._cur].isspace()):
            self._cur += 1
        return self._cur < len(self._buf)

    def _set_on_first_not_space(self):
        while self._cur < len(self._buf) and self._buf[self._cur].isspace():
            self._cur += 1
        return self._cur < len(self._buf)

    def _move_to_not_space(self):
        while not self._eof and not self._set_on_first_not_space():
            self._read_next_part()
        return not self._eof

    def _get_next_part(self):
        if not self._read_next_part():
            return 0
        if self._buf[0].isspace():
            return 0
        pos1 = self._cur
        parts = 1 + (not self._set_on_first_space())
        pos2 = self._cur
        self._parts.append(self._buf[pos1: pos2])
        return parts

    def _read_next_part(self):
        self._buf = self._f.readline(self._LEN)
        self._cur = 0
        self._eof = not self._buf
        return not self._eof

    def __enter__(self):
        return self

    def __del__(self):
        self.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._f.close()
        self._buf = ''
        self._eof = True

    def __iter__(self):
        return self

    def __next__(self):
        res = self.read()
        if res is None:
            raise StopIteration
        return res
