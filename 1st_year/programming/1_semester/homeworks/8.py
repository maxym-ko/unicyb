# 8_7
def point_input() -> float and float:
    x = input('Enter x: ')
    y = input('Enter y: ')
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        raise ValueError('x or y can not be represented as a real number')
    return x, y


# 8_8
def quadratic_equation_input():
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        raise ValueError('a or b or c can not be represented as a real number')
    print(f'{a}x^2 + {b}x + {c}')