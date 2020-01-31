# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle

for el in count(100):
    if el > 600:
        break
    else:
        print(el)

my_list = [1, 2, 3, 4]

c = 0
for el in cycle(my_list):
    if c > 100:
        break
    print(el)

    c += 1