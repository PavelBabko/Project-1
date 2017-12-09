import pickle
from bs4 import BeautifulSoup
import urllib.request
import time
import datetime
import sqlite3


url = 'https://www.kinopoisk.ru/box/weekend/2017-10-20/type/rus/cur/RUB/'

rezult = []

path2 = 'base.db'

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
	
	
sql1 = """
CREATE TABLE IF NOT EXISTS weeks(
        [index] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    	  date DATE,
        sumTotal TEXT,
        countOfViewers TEXT,
        link TEXT      
        )
"""


sql2 = """
CREATE TABLE IF NOT EXISTS films(
        links TEXT PRIMARY KEY,
        name TEXT,
        w_start INTEGER,
        w_end INTEGER
        )
"""

def extraction(url, n_week):
    response = urllib.request.urlopen(url)
    html = response.read()
    
    soup = BeautifulSoup(html, "html.parser")
    
    rez1 = soup.find_all('td', class_='news')
    rez2 = soup.find_all('dd', class_ = ['pls', 'mns'])

    print(rez2)
    
    next_link = 'https://www.kinopoisk.ru' + rez1[0].find('a').attrs['href']
    count_of_viewers = rez2[0].find('i').text
    summ_total = rez2[1].find('i').text
    
    date =  url.split('/')[5]
    year = date.split('-')[0]
    month = date.split('-')[1]
    day = date.split('-')[2]
    
    date = datetime.date(int(year), int(month), int(day))
    print(n_week)
    links = []
    names = []
    attrs = []
    for i in range(2, 12):
        links.append('https://www.kinopoisk.ru/' + rez1[i].find('a').attrs['href'])
        names.append(rez1[i].find('a').text)
        attrs.append(rez1[i].find('a').attrs['class'][0])
		  
        sql = """
        SELECT * FROM films WHERE links=\'{}\'
        """.format(links[-1])
        
        rez = select(path2, sql)
        print(len(rez))
        if len(rez) == 0:            
            sql = '''
            INSERT INTO films(links, name, w_start, w_end)
            values(\'{}\', \'{}\', {}, {})
            '''.format(links[-1], names[-1], n_week, n_week)
            print(sql)
            execute_sql(path2, sql)
            
			
        else:
            print(rez)
            print(rez[0][2]+1)
            sql = """
            UPDATE films
            SET w_start={} 
            WHERE links=\'{}\'            
            """.format(rez[0][2]+1, links[-1])
            execute_sql(path2, sql)

    
    rezult = {'link':url,
              'date': date,
              'count_of_viewers': count_of_viewers,
              'summ_total': summ_total,
              'links': links,
              'names': names,
              'attrs': attrs}    
    
    return(rezult, next_link)
    
if __name__ == "__main__":
    
    execute_sql(path2, sql1)
    execute_sql(path2, sql2)
    rez, next_link = extraction(url, 1)
    
    rezult.append(rez)
    time.sleep(3)

    for i in range(500):
        print(i)
        print(next_link)
        rez, next_link = extraction(next_link, i + 2)
        sql = '''
        INSERT INTO weeks(date, sumTotal, countOfViewers, link) 
        values (\'{}\', \'{}\', \'{}\', \'{}\')'''.format(rez['date'], rez['summ_total'], rez['count_of_viewers'], rez['link'])
        print(sql)
        execute_sql(path2, sql)
        rezult.append(rez)
        time.sleep(1)
		
        
    
    with open('rezult.picle', 'wb') as f:
        pickle.dump(rezult, f)
