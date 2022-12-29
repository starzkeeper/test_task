import pandas as pd
import sqlite3

conn = sqlite3.connect('parser.sqlite')
cur = conn.cursor()

df = pd.read_excel('Задание бек.xlsx')

df = df.drop(labels=[0, 1])
df = df.rename(columns={
    'fact': 'data1(Qliq(fact))',
    'Unnamed: 3': 'data2(Qliq(fact))',
    'Unnamed: 4': 'data1(Qoil(fact))',
    'Unnamed: 5': 'data2(Qoil(fact))',
    'forecast': 'data1(Qliq(forecast))',
    'Unnamed: 7': 'data2(Qliq(forecast))',
    'Unnamed: 8': 'data1(Qoil(forecast))',
    'Unnamed: 9': 'data2(Qoil(forecast))'
})

df.to_sql(name='Table1', con=conn, index=False)
