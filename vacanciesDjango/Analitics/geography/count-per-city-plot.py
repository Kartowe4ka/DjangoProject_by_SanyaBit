import json
import matplotlib.pyplot as plt


with open('count_per_city.json', encoding="utf_8") as file:
    data = json.load(file)

cities = []
counts = []
for city, count in data.items():
    cities.append(city)
    counts.append(count)

total = sum(data.values())
labels = [f"{n} ({v/total:.1%})" for n,v in zip(data.keys(), data.values())]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (1000 / dpi, 600 / dpi) )


plt.title('Доля вакансий по городам')

plt.pie(
    data.values(), radius=1.1,
    explode=[0.15] + [0 for _ in range(len(data.keys()) - 1)] )
plt.legend(
    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
    loc = 'center', labels = labels )
plt.show()

# plt.pie(counts, labels=cities)
# plt.title("Доля вакансий по городам")
# plt.show()