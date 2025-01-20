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


for index, row in C1_vacancies[['salary_from', 'salary_to', 'salary_currency', 'published_at']].dropna().iterrows():
    if row['salary_currency'] == "RUR":
        salary = int((row['salary_from'] + row['salary_to']) / 2)
        print(row['salary_from'], row['salary_to'], salary, row["salary_currency"], row["published_at"])
    else:
        excel = openpyxl.load_workbook(f'../currencies/{row['salary_currency']}.xlsx').active
        currency = get_currency(excel, str(row['published_at'])[:7])
        salary = int((row['salary_from'] + row['salary_to']) / 2) * currency
        print(row['salary_from'], row['salary_to'], salary, currency, row["salary_currency"], row["published_at"])

    if salary < 10000000:
        if str(row['published_at'])[:4] not in res.keys():
            res[str(row['published_at'])[:4]] = [salary]
        else:
            res[str(row['published_at'])[:4]].append(salary)

result = {
    "1st_column": "Год",
    "2nd_column": "Средняя зарплата",
    "data": {}
}
for key, value in res.items():
    result['data'][key] = int(sum(value) / len(value))

print(result)


with open("salary_per_year1.json", "w", encoding='utf-8') as outfile:
    json.dump(result, outfile, ensure_ascii=False)
