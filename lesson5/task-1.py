# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.


with open('text_task1.txt', 'a') as file:
    while True:
        user_input = input('Enter your input, when done, press carriage return: ')
        if user_input == '':
            break
        else:
            file.write(user_input + '\n')
