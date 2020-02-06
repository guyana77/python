file = open('text_task7.txt', encoding='utf-8')

for line in file:
    profit = (int(line.split()[2]) - int(line.split()[3]))

# никак не успеть доделать