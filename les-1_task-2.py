# Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input('Please, enter time in seconds: '))
hours = time // 600
minutes = (time % 600) // 60
seconds = (time % 600) % 60
print(f'Your time in hh:mm:ss format: {hours:02d}:{minutes:02d}:{seconds:02d}')
