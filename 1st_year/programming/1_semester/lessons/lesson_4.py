def f(x, y):
    z = None
    if x <= 0:
        z = x + 2
    elif x <= 3:
        z = x - y
    else:
        z = x + y
    return z


def f_2(a, b):
    if a == 0 and b == 0:
        return -1
    elif a == 0 and b != 0:
        return 0
    else:
        return 1
