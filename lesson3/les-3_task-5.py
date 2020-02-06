# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.

def my_sum():
    intermediate_sum = 0
    while True:
        list = input('Введите ряд чисел, разделенных пробелами, или введите # для завершения: ')
        if list[0] == '#':
            print('Выход')
            break
        elif '#' in list:
            list = list[:list.index('#') - 1]
            result = eval(list.replace(' ', '+')) + intermediate_sum
            print(f'Сумма равна {result}')
            break

        else:
            result = eval(list.replace(' ', '+')) + intermediate_sum
            intermediate_sum = result
            print(f'Сумма равна {result}')


my_sum()
