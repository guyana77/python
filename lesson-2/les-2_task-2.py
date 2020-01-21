# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

list = [15, True, 17.68, {1: 'Hello', 2: 'World'}, 'python is the best', {1, 2, 3, 4 ,5}, (True, 'hello', 15)]

last_element = len(list) - 1 if len(list) % 2 else len(list)
list[1:last_element:2], list[:last_element:2] = list[:last_element:2], list[1:last_element:2]

print(list)