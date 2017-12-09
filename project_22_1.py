import sqlite3
import pickle
import pandas as pd

def select(db_name, sql):
    conn = sqlite3.connect(db_name)
    cursor = conn.execute(sql)
    rez = cursor.fetchall()    
    conn.close()
    return rez

def execute_sql(db_name, sql):
    conn = sqlite3.connect(db_name)
    cursor = conn.execute(sql)  
    conn.commit()
    conn.close()

path1 = 'rezult.picle'


with open(path1, 'rb') as f:
    rez = pickle.load(f)
    
    
path2 = 'base.db'


sql1 = """
CREATE TABLE IF NOT EXISTS weeks(
        [index] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        day INTEGER,
        month INTEGER,
        year INTEGER,
        sumTotal TEXT,
        countOfViewers TEXT,
        link TEXT      
        )
"""


sql2n = """
CREATE TABLE IF NOT EXISTS films(
        [index] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT,
        links TEXT,
        w_start INTEGER,
        w_end INTEGER
        )
"""

sql3n = """
INSERT INTO films(
                  name,
                  links,
                  w_start,
                  w_end
                 ) 
values(\'{}\', \'{}\', {}, {})
"""

sql3 = """
INSERT INTO weeks(
                  day,
                  month,
                  year,
                  sumTotal,
                  countOfViewers,
                  link  
                 ) 
values({}, {}, {}, \'{}\', \'{}\', \'{}\')
"""


sql5 = """
SELECT day, month, year, link FROM weeks WHERE "index">4 AND "index"<9
"""

        
execute_sql(path2, sql1)

execute_sql(path2, sql2n)

links = []
for i in rez:
    rr = set(i['links'])
    for k in rr:
        links.append(k)
        
links = set(links)

result = pd.DataFrame(columns=['name', 'link', 'week'])

z=0

for i, j in enumerate(rez):
    print(j)
    for k, n in enumerate(j['names']):
        print(i, k, i+k)
        result.loc[z] = [n, j['links'][k], i+1]
        z=z+1
        
for i in links:
    print(i)
    film = result[result['link']==i] 
    film = film.reset_index(drop=True)
    name = film['name'][0]
    w_start = int(film['week'].min())
    w_end = int(film['week'].max())
    execute_sql(path2, sql3n.format(name, i, w_start, w_end))


for j, i in enumerate(rez):
    command1 = sql3.format(i['day'], i['month'], i['year'], 
                        i['summ_total'], i['count_of_viewers'], 
                        i['link'])
    print(command1)
    print(j)
    execute_sql(path2, command1)
        
print(select(path2, sql5))
