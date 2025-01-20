import pandas as pd
import json
import openpyxl

vacancies = pd.read_csv('../vacancies_2024.csv')
C1_vacancies = vacancies[vacancies['name'].str.contains('1C', case=False, na=False)]
res = {}


def get_currency(excel, date):
    for row in excel:
        if str(row[1].value)[:7] == date:
            return int(row[2].value / row[0].value)


for index, row in C1_vacancies[['salary_from', 'salary_to', 'salary_currency', 'published_at', 'area_name']].dropna().iterrows():
    if row['salary_currency'] == "RUR":
        salary = int((row['salary_from'] + row['salary_to']) / 2)
        print(row['salary_from'], row['salary_to'], salary, row["salary_currency"], row["published_at"])
    else:
        excel = openpyxl.load_workbook(f'../currencies/{row['salary_currency']}.xlsx').active
        currency = get_currency(excel, str(row['published_at'])[:7])
        salary = int((row['salary_from'] + row['salary_to']) / 2) * currency
        print(row['salary_from'], row['salary_to'], salary, currency, row["salary_currency"], row["published_at"])

    if salary < 10000000:
        if row['area_name'] not in res.keys():
            res[row['area_name']] = [salary]
        else:
            res[row['area_name']].append(salary)


res1 = {}
for key, value in res.items():
    if len(value) < 50:
        continue
    res1[key] = int(sum(value) / len(value))

res_sort = dict(sorted(res1.items(), key=lambda item: item[1], reverse=True))

result = {
    '1st_column': 'Город',
    '2nd_column': 'Зарплата',
    'data': {}
}
k = 0
for key, value in res_sort.items():
    k += 1
    if k == 20:
        break
    result['data'][key] = value

with open("salary_per_city2.json", "w", encoding='utf-8') as outfile:
    json.dump(result, outfile, ensure_ascii=False)
