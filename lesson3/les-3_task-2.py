# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def personal_info():
    name = input('Enter your name: ')
    surname = input('Enter your surname: ')
    place_of_residence = input('Enter your city of residence: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone number: ')
    return print(f'You are {name} {surname}, you live in {place_of_residence}, '
                 f'we can contact you by email {email} and phone number {phone}')

personal_info()