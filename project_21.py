import pickle
from bs4 import BeautifulSoup
import urllib.request
import time


url = 'https://www.kinopoisk.ru/box/weekend/2017-10-20/type/rus/cur/RUB/'

rezult = []

def extraction(url):
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
    
    links = []
    names = []
    attrs = []
    for i in range(2, 12):
        links.append('https://www.kinopoisk.ru/' + rez1[i].find('a').attrs['href'])
        names.append(rez1[i].find('a').text)
        attrs.append(rez1[i].find('a').attrs['class'][0])
    
    rezult = {'link':url,
              'count_of_viewers': count_of_viewers,
              'summ_total': summ_total,
              'links': links,
              'names': names,
              'attrs': attrs, 
              'year': year,
              'month': month,
              'day': day}    
    
    return(rezult, next_link)
    
if __name__ == "__main__":
    
    rez, next_link = extraction(url)
    
    rezult.append(rez)
    time.sleep(1)
    for i in range(500):
        print(i)
        print(next_link)
        rez, next_link = extraction(next_link)
        rezult.append(rez)
        time.sleep(1)
        
    
    with open('rezult.picle', 'wb') as f:
        pickle.dump(rezult, f)
