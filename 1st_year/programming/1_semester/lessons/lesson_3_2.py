def info_author():
    about_author = f"\
    Виконавець: Коваль\n\
                Максим\n\
                Романович\n\
    Група: К-12\n"
    print(about_author)


print('Ця програма обчиснює суму двох дійсних чисел.')
info_author()

x = float(input('Введіть перше дійсне число: '))
y = float(input('Введіть друге дійсне число: '))

print(f'\nВи ввели наступні значення: x = {x}, y = {y}\n')

res = x + y

print('Результат:', res)