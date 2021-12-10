# def f_0(n):
#     print(n % 10, end='')
#     if n > 1:
#         f_0(n // 10)
#
#
# def f(n):
#     if n < 0:
#         print('-', end='')
#         n = -n
#     f_0(n)
#
#
# f(-15790)
#
#
# def rev(n):  # f(n, k) = f(n, k-1)*10 + a(k)
#     res = 0
#     while n > 0:
#         res *= 10
#         res += n % 10
#         n //= 10
#     return res
#
#
# print(rev(123456789))


def root(f, a, b, eps=10E-7):
    c = (a + b) / 2
    f_c = f(c)
    if f_c == 0:
        return c
    if f_c > 0:
        if f(a) > 0:
            return root(f, c, b)
        else:
            return root(f, a, c)
    else:
        if f(a) < 0:
            return root(f, c, b)
        else:
            return root(f, a, c)


def root(f, a, b, eps=10E-7):
    up = f(a) < a
    fc = 1
    c = a
    while b - a >= eps and fc != 0.0:
        c = (a + b) * 0.5
        fc = f(c)
        if fc > 0.0:
            if up:
                a = c
            else:
                b = c

        else:
            if up:
                b = c
            else:
                a = c
        return c


print()