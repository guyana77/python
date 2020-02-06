# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров...

a = float(input('Enter the distance in kilometers you ran on your first day: '))
b = float(input('Enter the distance you are willing to run in a few training days: '))

daynumber = 1

while a < b:
    daynumber += 1
    a = (a + a * 0.1)
print(daynumber)
