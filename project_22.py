import pickle
import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


def str_to_int(string):
    pr = rezult[i]['count_of_viewers']
    string = string.replace(' руб.', '')
    string = string.split(' ')
    string = string[0].replace('\xa0', '')
    pr = int(string)
    #print(pr)
    return(pr)


if __name__ == "__main__":
    with open('rezult.picle', 'rb') as f:
        rezult = pickle.load(f)

       
    price = []
    count = []
    aver_price = []
    date = []
    for i in range(len(rezult)):
        index = len(rezult) - i - 1
        pr = str_to_int(rezult[index]['count_of_viewers'])
        count.append(pr)
        pr = str_to_int(rezult[index]['summ_total'])
        price.append(pr)
        aver_price.append(price[-1]/count[-1])
        date.append(datetime.datetime(int(rezult[index]['year']),
                  int(rezult[index]['month']), int(rezult[index]['day'])))
        
        
        
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
