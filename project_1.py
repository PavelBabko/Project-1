
import urllib.request

from bs4 import BeautifulSoup

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
    extraction(get_html('https://www.kinopoisk.ru/premiere/ru/2015/'))

if __name__ == '__main__':
    main()
