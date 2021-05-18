import requests
from bs4 import BeautifulSoup
import csv


url = 'http://books.toscrape.com/catalogue/forever-and-forever-the-courtship-of-henry-longfellow-and-fanny-appleton_894/index.html'
#book url

url_i = 'http://books.toscrape.com/'
#to define the path for the url of book image

#create the headers of csvfile
with open('onebook.csv', 'w', newline='', encoding='utf-8-sig') as books:
        bookswriter = csv.writer(books, delimiter=',', dialect='excel')

        bookswriter.writerow(
        ['product_page_url', 'universal_product_code',
         'title', 'price_including_tax'
            , 'price_excluding_tax', 'number_available',
         'product_description', 'category',
         'review_rating', 'image_url'])



def get_a_book(url):
    """get book information"""
    response = requests.get(url)
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
        product_page_url = url
        image = soup.img['src'].replace('../../', '')
        image_url = url_i + image
        category = a[2].text

        #load data on csv file
        with open('onebook.csv', 'a', newline='', encoding='utf-8-sig') as books:
            bookswriter = csv.writer(books, delimiter=',', dialect='excel')

            bookswriter.writerow([product_page_url, upc,
                                  title, price_including_tax,
                                  price_excluding_tax, number_available
                                     , product_description, category
                                     , review_rating, image_url])



get_a_book(url)