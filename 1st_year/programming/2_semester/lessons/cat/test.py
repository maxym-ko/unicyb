from cat import Cat

_menu = {'1': ('run', Cat.run), '2': ('sleep', Cat.sleep), '3': ('eat', Cat.run)}


def ask_action(tom):
    print(tom)
    menu(_menu)
    s = input('Select action: ')
    s = check_action(s)
    return s


def check_action(s):
    if not s or s == '0':
        return 0
    else:
        return s


def do_action(tom, action, _menu):
    if action in _menu:
        _menu[action][1](tom)


def menu(_menu):
    for key, item in _menu.items():
        print(key, item[0])


tom = Cat(10.0)
action = ask_action(tom)

while action:
    do_action(tom, action, _menu)
    action = ask_action(tom)
