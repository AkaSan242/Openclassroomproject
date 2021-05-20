import requests
from bs4 import BeautifulSoup
import csv
from getbook import get_a_book
from getbookslink import get_books_links

"""Script to scrape the website 'books.toscrape.com'"""

url = 'http://books.toscrape.com/index.html'
#website url

category_path = 'http://books.toscrape.com/'
#use to create the link for a category url

category_urls = []
#to keep the categories urls on a list and use them to find all books urls

books_urls = []
#use to get books informations and write them on a csvfile for each category


def get_category(url):

    #to extract the link of all categories
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        ul = soup.find('ul', {'class': 'nav nav-list'}).find_all('a')

        for link in ul:
            links = link.get('href')
            category_url = category_path + links
            category_urls.append(category_url)

        #create csvfile for all categories
        for i in range(len(ul)):
            with open('{}.csv'.format(ul[i].text.strip()), 'w', newline='', encoding='utf-8-sig') as books:
                bookswriter = csv.writer(books, delimiter=',', dialect='excel', quoting=csv.QUOTE_ALL)

                # to create the Headers of the csv file
                bookswriter.writerow(
                        ['product_page_url', 'universal_product_code',
                         'title', 'price_including_tax'
                            , 'price_excluding_tax', 'number_available',
                         'product_description', 'category',
                         'review_rating', 'image_url'])


get_category(url)
#get all category links and create a csvfile for each category

del category_urls[0]
#we dont need the main page

for url in category_urls:
    get_books_links(url, books_urls)
#Get all books link in one category

print('il y a "{}" livres sur le site Bookstoscrape et "{}" catégories'.format(len(books_urls), len(category_urls)))
# to check if i have all 1000 books

for url in books_urls:
    get_a_book(url)
#get book informations and write them in his category csvfile



