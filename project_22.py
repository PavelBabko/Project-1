import pickle
import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import sqlite3
import datetime

path2 = 'base.db'

def select(db_name, sql):
    conn = sqlite3.connect(db_name)
    cursor = conn.execute(sql)
    rez = cursor.fetchall()    
    conn.close()
    return rez

def str_to_int(string):
    pr = rezult[i][3]
    string = string.replace(' руб.', '')
    string = string.split(' ')
    string = string[0].replace('\xa0', '')
    pr = int(string)
   #print(pr)
    return(pr)


if __name__ == "__main__":
    with open('rezult.picle', 'rb') as f:
        rezult = pickle.load(f)
        
    sql="""SELECT * FROM weeks"""
    rezult = select(path2, sql)
    print(rezult[0])
    price = []
    count = []
    aver_price = []
    date = []
    for i in range(len(rezult)):
        index = len(rezult) - i - 1
        pr = str_to_int(rezult[index][3])
        count.append(pr)
        pr = str_to_int(rezult[index][2])
        price.append(pr)
        aver_price.append(price[-1]/count[-1])
        date.append(datetime.datetime.strptime(rezult[index][1], '%Y-%m-%d'))
        #date.append(datetime.datetime(int(rezult[index]['year']),
        #           int(rezult[index]['month']), int(rezult[index]['day'])))
         
         
         
    res = seasonal_decompose(price, model='multiplicative', freq=12*4)
    
     
    plt.plot(date, price, label='сборы за уик-энд')
    plt.legend(loc='upper left')
    plt.show()
    plt.plot(date, count, label='число зрителей')
    plt.legend(loc='upper left')
    plt.show()
    plt.plot(date, aver_price, label='средняя цена')
    plt.legend(loc='upper left')
    plt.show()
    res.plot()
    plt.show()
