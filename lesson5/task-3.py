# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

file = open('text_task3.txt', encoding='utf-8')
surnames_less20 = []
salary_less20 = []
salaries = []
for line in file:
    surname = line.split(' ', 1)[0]
    salary = float(line.split(' ', 2)[1].split('\n')[0])
    if salary <= 20000:
        surnames_less20.append(surname)
        salary_less20.append(salary)
    salaries.append(salary)

print(f'Employees {surnames_less20} get lestt than 20k. Their slaries are {salary_less20} respectively')
print(f'Average salay in the company is: {sum(salaries) / len(salaries):.2f}')

file.close()
