import requests
from bs4 import BeautifulSoup

class CryptoScrapper:
    def data_retriever(self, crypto):
        url_link = 'https://coinmarketcap.com/currencies/' +crypto+ '/news/'
        request = requests.get(url_link, 'html.parser').text
        beautiful_soup = BeautifulSoup(request,'lxml')
        paragraph_heading = beautiful_soup.h1.text
        print(paragraph_heading)

        paragraph = beautiful_soup.text.strip()
        x = 0

        for i in range(len(paragraph)):
        
            print (paragraph[i], end ='')
            if paragraph[i] ==' ':
                x = x + 1
            if x == 5:
                print('\n', end='')
                x = 0
        print()
        
