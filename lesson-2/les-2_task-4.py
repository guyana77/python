# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

list = list(input('Enter several words spaced: ').split(' '))
# count = 1
# for item in list:
#     print(f'{count}. {item}')
#     count += 1

for index, item, in enumerate(list, 1):
    print(index, item)