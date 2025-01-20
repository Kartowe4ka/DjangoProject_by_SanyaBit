import matplotlib.pyplot as plt
import json

with open('salary_per_year.json') as file:
    data = json.load(file)

years = []
salaries = []
for year, salary in data.items():
    years.append(year)
    salaries.append(salary)

plt.bar(years, salaries)
plt.xticks(rotation = 90)
plt.title("Динамика уровня зарплат по годам")
plt.show()
