import requests
from bs4 import BeautifulSoup
import csv


book_url = 'http://books.toscrape.com/catalogue/forever-and-forever-the-courtship-of-henry-longfellow-and-fanny-appleton_894/index.html'

url = 'http://books.toscrape.com/'
#to define the path for the url of book image



def get_status(book_url):
    #check url status
    response = requests.get(book_url)
    if response.ok:
        print(response.status_code)
    else:
        print('no news')


def get_a_book(book_url):
    """get book information"""
    response = requests.get(book_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        #to read the doc and find the information

        #extract book informations
        td = soup.findAll('td')
        p = soup.findAll('p')
        a = soup.ul.find_all('a')

        #transform book informations
        title = soup.h1.text
        product_description = p[3].text.replace(',', '.')
        upc = td[0].text
        price_excluding_tax = td[2].text
        price_including_tax = td[3].text
        number_available = td[5].text
        review_rating = td[6].text
        product_page_url = book_url
        image = soup.img['src'].replace('../../', '')
        image_url = url + image
        category = a[2].text

        #load information on csvfile
        with open('book.csv', 'w', newline='', encoding='utf-8-sig') as books:
            books.write(
                'product_page_url,' + 'universal_product_code,'
                 + 'title,' + 'price_including_tax,'
                + 'price_excluding_tax,' + 'number_available,'
            + 'product_description,' + 'category,'
                + 'review_rating,' + 'image_url' + '\n')

            books.write(product_page_url + ',' + upc + ','
                    + title + ',' + price_including_tax + ','
                    + price_excluding_tax + ',' + number_available
                    + ',' + product_description + ',' + category
                    + ',' + review_rating + ',' + image_url + '\n')


get_status(book_url)
get_a_book(book_url)
