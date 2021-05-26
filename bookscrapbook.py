import requests
from bs4 import BeautifulSoup
import csv
from bookscraplib import get_a_book


url = 'http://books.toscrape.com/catalogue/forever-and-forever-the-courtship-of-henry-longfellow-and-fanny-appleton_894/index.html'
#book url


response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.content, 'html.parser')
    # to read the doc and find the information

    a = soup.ul.find_all('a')
    category = a[2].text


    #create the headers of csvfile
    with open('csvfiles/{}.csv'.format(category), 'w', newline='', encoding='utf-8-sig') as books:
        bookswriter = csv.writer(books, delimiter=',', dialect='excel')

        bookswriter.writerow(
        ['product_page_url', 'universal_product_code',
         'title', 'price_including_tax'
            , 'price_excluding_tax', 'number_available',
         'product_description', 'category',
         'review_rating', 'image_url'])


get_a_book(url)