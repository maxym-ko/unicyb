import math


# 9_10
def f(m):
    a_n, a, b = 0, 1, 1
    while a_n <= m:
        a_n = 2 * a + 3 * b
        b, a = a, a_n
    return a_n


# 9_11
def f(n):
    a, b, a_k = 1, 1, 1
    while n != 1:
        b_k = a % b + 2 * a
        a_k = b * a + 2 * a
        a, b = a_k, b_k
        n -= 1
    return a_k


# 9_14b
def f():
    n, res = int(input()), 1
    for k in range(1, n + 1):
        res = res * (n - k + 1) // k
        print(res)


# 9_14c
def f():
    n, k, res = int(input()), 1, 1
    print(res)
    while k != n + 1:
        res *= (n / k) + 1
        print(int(res))
        k += 1


# 9_17
def f(a, b, h=10e-5):
    res = math.sin(math.cos(13 * b)) + math.cos(math.log(b))
    while b > a:
        tmp = math.sin(math.cos(13 * b)) + math.cos(math.log(b))
        if tmp > res:
            res = tmp
        b -= h
    return res
