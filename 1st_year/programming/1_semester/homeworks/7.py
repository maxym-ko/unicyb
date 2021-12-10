import math


# 7_25a
def is_perpendicular_lines(a1: float, b1: float, a2: float, b2: float) -> bool:
    if a1 * a2 + b1 * b2 == 0:
        return True
    return False


# 7_25b
def is_collinear_lines(a1: float, b1: float, a2: float, b2: float) -> bool:
    if a1 * b2 == a2 * b1:
        return True
    return False


# 7_12
a, b, c, d = 1, 1, 1, 1
print(a == b == c == d)  # a
print(a != b != c != d)  # б
print(a != b or a != c or a != d or b != c or b != d or c != d)  # в


# 7_21
a, b, c, d = 1, 4, 2, 3
print(c > b or d < a)  # а
print(c == b or d == a)  # б
print(a < c < b or a < d < b)  # в


# 7_16
a, b = 19, 13
print(b % 3 == 0)  # а
print(isinstance(b, float))  # б (хз чи це мали на увазі)
print(a % 2 == b % 2)  # в
print(a % b == 0)  # г


# 7_17
def float_equal(a: float, b: float, e: float = 1.e-7) -> bool:
    return math.fabs(a - b) < e


# 7_38
def foo(x: float) -> bool:
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


# 7_42
def count_root(a: float, b: float, c: float) -> int:
    if a == b == c == 0:
        return -1
    d = b ^ b - 4 * a * c
    if d == 0:
        return 1
    elif d < 0:
        return 0
    else:
        return 2