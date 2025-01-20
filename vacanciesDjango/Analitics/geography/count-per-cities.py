import pandas as pd
import json
from itertools import islice

vacancies = pd.read_csv('../vacancies_2024.csv')
C1_vacancies = vacancies[vacancies['name'].str.contains('1C', case=False, na=False)]


res = {}
count = 0
for column in C1_vacancies['area_name']:
    if pd.isna(column):
        continue
    if column in res.keys():
        res[column] += 1
        count += 1
    else:
        res[column] = 1
        count += 1


res_sort = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))

result = {
    '1st_column': 'Город',
    '2nd_column': 'Количество',
    'data': {}
}
k = 0
count = 0
for key, value in res_sort.items():
    k += 1
    if k == 20:
        break
    result['data'][key] = value
    count += value

for key, value in result['data'].items():
    result['data'][key] = str(round((round(result['data'][key] / count, 5) * 100), 1)) + "%"
print(result)

with open("count_per_city.json", "w", encoding='utf-8') as outfile:
    json.dump(result, outfile, ensure_ascii=False)

