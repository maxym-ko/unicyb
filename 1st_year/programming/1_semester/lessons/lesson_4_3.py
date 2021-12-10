import math


def info_author():
    about_author = f"\
    Виконавець: Коваль\n\
                Максим\n\
                Романович\n\
    Група: К-12\n"
    print(about_author)


def func(x: float, y: float, z: float) -> float:
    """Return the value of e^x + 2yz"""

    res = math.exp(x) + 2 * y * z
    return res


print('Ця програма обчиснює значення формули e^x + 2yz')
info_author()

_x = float(input('Введіть значення x: '))
_y = float(input('Введіть значення y: '))
_z = float(input('Введіть значення z: '))

print(f'Ви ввели наступні значення: x = {_x}, y = {_y}, z = {_z}\n')

print(f'Обчислюється значення формули: e^{_x} + 2 * {_y} * {_z}')
_res = func(_x, _y, _z)

print('Результат:', f'{_res:.4f}')
