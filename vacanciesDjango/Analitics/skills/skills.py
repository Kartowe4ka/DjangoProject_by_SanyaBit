import pandas as pd
from collections import Counter
import json


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

data = {
    "1st_column": "Навык",
    "2nd_column": "Количество",
    "data": {}
}

data['data'] = dict(zip(skill, count))
print(data)

with open("res.json", "w", encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
