# Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше
# издержек, или убыток — издержки больше выручки)...

revenue = int(input("Enter your company's revenue: "))
costs = int(input("Enter your company's costs: "))

if revenue > costs:
    print(f'Your company is in profit of USD {revenue - costs}. \n'
          f'Your profit margin is {(revenue - costs) / revenue * 100:.2f}%')

elif revenue == costs:
    print('Your company is neither in loss, nor in profit')
else:
    print(f'Your company has suffered losses of USD {revenue - costs}')

if revenue > costs:
    headcount = int(input('Enter your staff headcount: '))
    print(f'Profit per employee in your company is USD {(revenue - costs) / headcount:.2f}')
