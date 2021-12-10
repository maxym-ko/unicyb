class R:
    def __init__(self):
        self._has = False

    def put(self):
        if self._has:
            return False
        else:
            self._has = True
            return True

    def get(self):
        if not self._has:
            return True
        else:
            self._has = True
            return False


obj = R()
for _ in range(10):
    s = input('...')
    if s == '1':
        res = obj.put
    elif s == '2':
        res = obj.get()
    else:
        res = None
    if res in None:
        print('...')
    elif res:
        print('OK')
    else:
        print('not OK')
