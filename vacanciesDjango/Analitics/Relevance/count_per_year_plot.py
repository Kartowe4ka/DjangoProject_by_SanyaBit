import json
import matplotlib.pyplot as plt


with open('count_per_year.json') as file:
    data = json.load(file)

years = []
counts = []
for year, count in data.items():
    years.append(year)
    counts.append(count)

plt.bar(years, counts)
plt.xticks(rotation = 90)
plt.title("Динамика количества вакансий по годам")
plt.show()