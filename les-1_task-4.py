# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Enter an integer positive number having several digits: '))
n_max = 0
last_digit = number % 10
while n_max <= last_digit:
    last_digit = number % 10
    if last_digit == 9:
        n_max = 9
        break
    if last_digit > n_max:
        n_max = last_digit
    number //= 10

print(f'Maximum digit in your number is {n_max}')


