from django.test import TestCase
import sys
from pprint import pprint
import os
import sqlite3
import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

# Create your tests here.
con = sqlite3.connect(r'C:\Users\79502\Desktop\python_bib\project\bombing\db.sqlite3')
cur = con.cursor()
# cur.execute('''CREATE TABLE class9
#               (
#    "id"    INTEGER UNIQUE,
#    "oid"    INTEGER DEFAULT 0 UNIQUE,
#    "characters"    TEXT,
#    "about"    TEXT,
#    PRIMARY KEY("id" AUTOINCREMENT)
# )''')
# Insert a row of data

text_news_in_base = []
for row in cur.execute('SELECT * FROM bombing_info'):  # ORDER BY importance DESC'):
    text_news_in_base.append(row[4])
    # self.stdout.write(row[4])
    # print(row[6])

sys.path = [r'C:\Users\79502\Desktop\python_bib\newsportal-Julianna-fil-main\site\miner\reporters'] + sys.path

reporters = os.listdir(r'C:\Users\79502\Desktop\python_bib\newsportal-Julianna-fil-main\site\miner\reporters')

import pandas as pd

df = pd.read_excel(r'C:\Users\79502\Desktop\python_bib\project\bombing\web_app\actual.xlsx')
for i in range(len(df)):
    df.loc[i, 'coordinates1'] = float(str(df.loc[i, 'coordinates1']).replace(',', '.'))
    df.loc[i, 'coordinates2'] = float(str(df.loc[i, 'coordinates2']).replace(',', '.'))
df['coordinates1'] = pd.to_numeric(df['coordinates1'], errors='coerce')
df['coordinates2'] = pd.to_numeric(df['coordinates2'], errors='coerce')
df['№ п/п'] = pd.to_numeric(df['№ п/п'], errors='coerce', downcast='integer')
df['ФАБ'] = pd.to_numeric(df['ФАБ'], errors='coerce', downcast='integer')
df['ЗАБ'] = pd.to_numeric(df['ЗАБ'], errors='coerce', downcast='integer')
df['Снаряд'] = pd.to_numeric(df['Снаряд'], errors='coerce', downcast='integer')
df['Убито'] = pd.to_numeric(df['Убито'], errors='coerce', downcast='integer')
df['Ранено'] = pd.to_numeric(df['Ранено'], errors='coerce', downcast='integer')

df.fillna(0)
df = df.astype({"Ранено": "Int64", "Убито": "Int64", "Снаряд": "Int64", "ЗАБ": "Int64", "ФАБ": "Int64"})


try:
    pass
except Exception as e:
            s = f'INSERT INTO miner_logs (time, reporter_file, reporter_name, text) VALUES ("{time}", "{r}", "{m.name}", "{e}")'
            cur.execute(s)


for i in range(len(df)):
    id_act = df.loc[i, 'Unnamed: 0']
    id_old = df.loc[i, 'Unnamed: 0.1']
    num_pp = df.loc[i, '№ п/п']
    num_report = df.loc[i, '№ сводки']
    date = df.loc[i, 'Дата']
    district = df.loc[i, 'Район']
    street_and_house = df.loc[i, 'Улица, дом']
    object_ = str(df.loc[i, 'Объект']).replace('\"','')
    high_explosive_AB = df.loc[i, 'ФАБ']
    incendiary_AB = df.loc[i, 'ЗАБ']
    projectile = df.loc[i, 'Снаряд']
    damage = str(df.loc[i, 'Причиненный ущерб']).replace('\"','')
    killed = df.loc[i, 'Убито']
    wounded = df.loc[i, 'Ранено']
    detection_time = df.loc[i, 'Время обнаружения']
    adress_act = df.loc[i, 'address']
    coordinates1 = df.loc[i, 'coordinates1']
    coordinates2 = df.loc[i, 'coordinates2']
    s = f'INSERT INTO web_app_info (id, id_old, num_pp, num_report, date, district, street_and_house, object, ' \
        f'high_explosive_AB, incendiary_AB, projectile, damage, killed, wounded, detection_time, adress_act, ' \
        f'coordinates1, ' \
        f'coordinates2) VALUES ({id_act}, {id_old}, {num_pp}, {num_report}, "{date}", "{district}", "{street_and_house}", "{object_}", ' \
        f'{high_explosive_AB}, {incendiary_AB}, {projectile}, "{damage}", {killed}, {wounded}, "{detection_time}", "{adress_act}", ' \
        f'{coordinates1}, ' \
        f'{coordinates2}) '
    print(s)
    cur.execute(s)

con.commit()
con.close()
