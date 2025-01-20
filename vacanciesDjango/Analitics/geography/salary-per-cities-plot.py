import matplotlib.pyplot as plt
import json

with open('salary_per_city2.json', encoding="utf_8") as file:
    data = json.load(file)

years = []
cities = []
for city, salary in data['data'].items():
    years.append(city)
    cities.append(salary)

plt.bar(years, cities)
plt.xticks(rotation = 90)
plt.title("Динамика уровня зарплат по городам")
plt.show()