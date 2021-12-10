# Переписати, згідно рекомендацій Карнаух
from greenhouse import Greenhouse

_menu = {'1': ('- open window', Greenhouse.open_window),
         '2': ('- close window', Greenhouse.close_window),
         '3': ('- switch on heater', Greenhouse.switch_on_heater),
         '4': ('- switch off heater', Greenhouse.switch_on_heater),
         '5': ('- time passed', Greenhouse.passed_time),
         '6': ('- stop', )}


def ask_action(greenhouse):
    print('\n', greenhouse)
    show_menu(_menu)
    action_selected = input('Select action: ')
    return check_action(action_selected)


def check_action(action_selected):
    if not action_selected or action_selected == '6':
        return 0
    else:
        return action_selected


def do_action(greenhouse, action, menu):
    if action in menu:
        print('\n', menu[action][1](greenhouse)[1])


def show_menu(_menu):
    for key, item in _menu.items():
        print(key, item[0])
    print()


_greenhouse = Greenhouse()
_action = ask_action(_greenhouse)

while _action:
    do_action(_greenhouse, _action, _menu)
    _action = ask_action(_greenhouse)

_greenhouse.stop()

print('You have stopped controlling the greenhouse')
