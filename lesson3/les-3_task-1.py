# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide():
    try:
        arg1 = int(input('Enter number 1:'))
        arg2 = int(input('Enter number 2, except 0:'))
    except ValueError:
        print('Number, not character, requred, try again')

    try:
        return arg1 / arg2
    except ZeroDivisionError:
        print('Division by zero unacceptable, try again')


print(divide(1, 0))