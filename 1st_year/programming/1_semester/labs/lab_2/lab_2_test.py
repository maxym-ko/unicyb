import math


def s_1(x):
    return 0.25 * math.log((1 + x) / (1 - x)) + 0.5 * math.atan(x)


def s_2(x, eps=10e-11):
    k = 5
    a_k = x
    _sum = a_k
    x_4 = x**4
    while math.fabs(a_k) >= eps:
        a_k *= x_4 * (k - 4) / k
        _sum += a_k
        k += 4
    return _sum


def f(a, b, step):
    while a <= b:
        if math.fabs(s_1(a) - s_2(a)) > 0.00001:
            print("Bad for ", a)
        a += step


_a, _b, _step = float(input()), float(input()), float(input())
f(_a, _b, _step)
