# 7. Реализовать генератор с помощью функции с ключевым словом yield,
from functools import reduce
from itertools import count

def fact(n):
    yield reduce(lambda a, b: a * b, [el for el in range(1, n + 1)])

n = 1
while True:
    for el in fact(n):
        if n > 15:
            break
        print(el)
        n += 1

# Что-то мне кажется я не то сделал, посмотрю потом разбор на следующем занятии
