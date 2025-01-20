import pandas as pd
import json

vacancies = pd.read_csv('../vacancies_2024.csv')
C1_vacancies = vacancies[vacancies['name'].str.contains('1C', case=False, na=False)]

res = {"1st_column": "Год",
       "2nd_column": "Количество",
       "data": {}
}
for column in C1_vacancies['published_at']:
    if pd.isna(column):
        continue
    year = column[:4]
    if year in res["data"].keys():
        res["data"][year] += 1
    else:
        res["data"][year] = 1

with open("count_per_year1.json", "w", encoding='utf-8') as outfile:
    json.dump(res, outfile, ensure_ascii=False)