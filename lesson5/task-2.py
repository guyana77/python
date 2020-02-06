# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open('text_task2.txt', 'r', encoding='utf-8')

num_lines = 0

for line in file:
    words = line.split()
    num_lines += 1
    print(f'Number of words in line {num_lines} is {len(words)}')

print(f'Number of lines in file: {num_lines}')

file.close()

