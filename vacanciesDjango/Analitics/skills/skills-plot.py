import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt


def sort_file(file_name):
    return file_name[file_name['name'].str.contains(name, case=False, na=False)]


def counter(file_name):
    skills = []
    for column in file_name['key_skills']:
        if pd.isna(column):
            continue
        skills.extend(column.split('\n'))
    count = Counter(skills)
    res = count.most_common(20)
    if sort_type == 'asc':
        res.sort(key=lambda x: x[1])
    else:
        res.sort(key=lambda x: x[1], reverse=True)
    return res


name = '1C'
sort_type = 'desc'
vacancies = pd.read_csv('../vacancies_2024.csv')
vacancies = sort_file(vacancies)

skill = []
count = []
for i in counter(vacancies):
    skill.append(i[0])
    count.append(i[1])

plt.bar(skill, count)
plt.xticks(rotation = 90)
plt.title("Количество упоминаний навыка")
plt.show()