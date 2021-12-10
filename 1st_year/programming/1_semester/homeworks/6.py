import math


# 6_4
a, b = 1, 2
res = math.log(math.hypot(a, b))  # а
res = math.sin(math.pow(a + b, 1 / 7))  # б
res = math.cos(math.pow(math.pow(a, 12) + math.pow(b, 12), 1 / 3))  # в
res = 1 / math.tan(math.fabs(math.sqrt(a) - math.sqrt(b)))  # г


# 6_7
def func(a, b):
    c = math.hypot(a, b)
    angle_a = math.asin(a / c)
    angle_b = math.asin(b / c)

    angle_a_degrees = math.degrees(angle_a)
    angle_b_degrees = math.degrees(angle_b)

    return angle_a, angle_b, angle_a_degrees, angle_b_degrees


# 6_12
def quadratic_equation():
    a = float(input('Input a: '))
    b = float(input('Input b: '))
    c = float(input('Input c: '))
    print(f"{a}x^2 + {b}x + {c} = 0")


# 6_13
def personal_greeting():
    surname = input('Enter tour surname: ')
    name = input('Enter tour name: ')
    print(f"Hello, {surname} {name}")


# 6_16
inf_1 = float('inf')
inf_2 = math.inf
negative_inf_1 = float('-inf')
negative_inf_1 = -math.inf
nan_1 = float('nan')
nan_2 = math.nan
