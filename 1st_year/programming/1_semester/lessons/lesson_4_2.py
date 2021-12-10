import math


def info_author():
    about_author = f"\
    Виконавець: Коваль\n\
                Максим\n\
                Романович\n\
    Група: К-12\n"
    print(about_author)


print('Ця програма обчиснює суму числа Пі та числа Ейлера')
info_author()

res = math.pi + math.e

print('Результат:', f'{res:.2f}')