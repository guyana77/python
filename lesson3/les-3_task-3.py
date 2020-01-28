# 3. Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    list = [arg1, arg2, arg3]
    list.remove(min(list))
    return sum(list)

print(my_func(4, 2, 9))
