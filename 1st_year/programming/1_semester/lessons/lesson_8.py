import math


# 10_24
def sum(x, eps=10e-8):
    x1, x2 = x, x * x * 0.5
    sum = x1 + x2
    last = x2
    k = 3
    flag = False
    while math.fabs(last) >= eps:
        if flag:
            x2 = x * x / k
            last = x2
        else:
            x1 = x * x / k
            last = x1
        sum += last
    return sum


# lab_2_example  (треба записати рекурентну формулу залежносты a_i від a_(i-1), порахувати преший елемент)
def sum(x, eps=10e-8):
    a = x
    sum = a
    k = 0
    x_sq = x * x
    while math.fabs(a) >= eps:
        a = (-a * x_sq) / (2*k * (2*k + 1))
        sum += a
        k += 1
    return sum
