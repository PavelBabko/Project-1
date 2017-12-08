import sqlite3
import pickle


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


sql2 = """
CREATE TABLE IF NOT EXISTS {}(
        [index] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT,
        links TEXT,
        attr TEXT   
        )
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

sql4 = """
INSERT INTO {}(
                name,
                links,
                attr 
              ) 
values(\'{}\', \'{}\', \'{}\')
"""

sql5 = """
SELECT day, month, year, link FROM weeks WHERE "index">4 AND "index"<9
"""

        
execute_sql(path2, sql1)


for j, i in enumerate(rez):
    command1 = sql3.format(i['day'], i['month'], i['year'], 
                        i['summ_total'], i['count_of_viewers'], 
                        i['link'])
    print(command1)
    print(j)
    execute_sql(path2, command1)
    execute_sql(path2, sql2.format('week{}'.format(j + 1)))
    for n, k in enumerate(i['names']):
        command2 = sql4.format('week{}'.format(j + 1), 
                               k, i['links'][n], i['attrs'][n])
        execute_sql(path2, command2)
        
print(select(path2, sql5))
