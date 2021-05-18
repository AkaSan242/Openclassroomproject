"""Script de la fonction get_a_book"""
import requests
from bs4 import BeautifulSoup
import csv

url_i = 'http://books.toscrape.com/'

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
        csvfile = '{}.csv'.format(category)

        #load on csv file
        with open(csvfile, 'a', newline='', encoding='utf-8-sig') as books:
            bookswriter = csv.writer(books, delimiter=',', dialect='excel')

            bookswriter.writerow([product_page_url, upc,
                                  title, price_including_tax,
                                  price_excluding_tax, number_available
                                     , product_description, category
                                     , review_rating, image_url])

        #to check the result while writing on csv
        print('livre: "{}", catégorie: "{}"'.format(title,category))