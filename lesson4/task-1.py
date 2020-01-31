# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import  argv

script_name, empl_norm, empl_hrate = argv

def salary(empl_norm, empl_hrate):
    try:
        result = int(empl_norm) * int (empl_hrate)
    except ValueError:
        return
    return result

print(f'Your salary is {salary(empl_norm, empl_hrate)}')
