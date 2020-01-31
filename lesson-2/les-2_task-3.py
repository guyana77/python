# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

months_dict = {1:'Winter',
               2:'Winter',
               3:'Spring',
               4:'Spring',
               5:'Spring',
               6:'Summer',
               7:'Summer',
               8:'Summer',
               9:'Autumn',
               10:'Autumn',
               11:'Autumn',
               12:'Winter'}

months_list = [None, 'Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']

user_month = int(input('Enter the month number from 1 to 12: '))

print(f'Your month is in {months_dict[user_month]}')
print(f'Your month is in {months_list[user_month]}')