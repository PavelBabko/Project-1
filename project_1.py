import urllib.request

from bs4 import BeautifulSoup

year=input('Введите интересующий год (не ранее 2000):')
month=input('Введите месяц в числовом эквиваленте:')
year1=str(year)
month1=str(month)
address=("https://www.kinopoisk.ru/premiere/ru/%s/month/%s/" % (year1,month1))

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def extraction(html):
    soup = BeautifulSoup(html,"html.parser")
    table = soup.find('div', class_ = 'block_left')
   
    filmoteka = []
    
    for film in table.find_all('span', class_ = 'name'):
        filmoteka.append(film.a.text)
        
    
    for i in filmoteka:
        print(i)
 
def main():
    
    extraction(get_html(address))


if __name__ == '__main__':
    main()
