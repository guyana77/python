# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import  randrange
with open('text_task5.txt', 'w+', encoding='utf-8') as file:
    file.write(' '.join(str(i) for i in range(-100, 100, 3)))

    print(sum(int(file.split(' '))))
