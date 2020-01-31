# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Please, enter any number: ')
result = int(f'{n}') + int(f'{n}{n}') + int(f'{n}{n}{n}')
print(result)
