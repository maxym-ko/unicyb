import math


def cmp(x: float, y: float) -> bool:
    if math.sin(x) == 0 or math.sin(y) == 0:
        return None
    return math.cos(x) / math.sin(x) - math.cos(y) / math.cos(y)


# 8_5
def foo():
    try:
        a = float(input('Enter a: '))
        b = float(input('Enter b: '))
        c = float(input('Enter c: '))
    except Exception:
        raise ValueError('not a number')
    if a == 0:
        raise ValueError('a shouldn\'t equal to zero')
    return a, b, c