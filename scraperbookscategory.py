import requests
from bs4 import BeautifulSoup
import csv
from bookscraplib import get_a_book,get_books_links


books_urls = []
#we'll use it to iterate on all category books links

url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
#category url

response = requests.get(url)
if response.ok:

    soup = BeautifulSoup(response.content, 'html.parser')
    category = soup.find('h1').text

    #Create csv file
    with open('csvfiles/{}.csv'.format(category), 'w', newline='', encoding='utf-8-sig') as books:
        bookswriter = csv.writer(books, delimiter=',', dialect='excel')

        # to create the Headers of the csv file
        bookswriter.writerow(
        ['product_page_url', 'universal_product_code',
         'title', 'price_including_tax'
            , 'price_excluding_tax', 'number_available',
         'product_description', 'category',
         'review_rating', 'image_url'])



get_books_links(url, books_urls)


#to compare with books numbers and check if we got all links
print('il y a "{}" livres dans books urls.'.format(len(books_urls)))


#add books on csv file
for url in books_urls:
    get_a_book(url)



