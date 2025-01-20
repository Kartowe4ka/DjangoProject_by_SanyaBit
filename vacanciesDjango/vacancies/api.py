import requests
import pandas as pd
import json
import time
from datetime import datetime


def get_page(page = 0):
    params = {
        'text': 'NAME:1C',
        'area': 113,
        'page': page,
        'per_page': 100
    }
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data


js_objs = []
for page in range(0, 5):
    js_obj = json.loads(get_page(page))
    js_objs.extend(js_obj["items"])
    if (js_obj['pages'] - page) <= 1:
        break
    time.sleep(0.05)


date = datetime.now().date()

df = pd.DataFrame(js_objs)[['name', 'area', 'salary', 'published_at', 'employer']].dropna()
df['published_at'] = pd.to_datetime(df['published_at']).dt.date
df = df.loc[df['published_at'] == date]
df['published_at'] = df['published_at']
df['area'] = df['area'].map(lambda a: a['name'])
df['salary'] = df['salary'].map(lambda a: a['from'])
df['salary'].fillna(int(df['salary'].mean()), inplace=True)
df['employer'] = df['employer'].map(lambda a: a['name'])
res = df.head(9)


def get_info():
    return res.to_dict('index')