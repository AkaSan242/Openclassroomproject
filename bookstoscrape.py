import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/index.html'

category_path = 'http://books.toscrape.com/'

category_urls = []

books_urls = []


def get_books_links(url):

    url_book_path = 'http://books.toscrape.com/catalogue/'
    # use to define the link of each book
    response = requests.get(url)
    next_path = url.replace('index.html', '')
    # use to create a path if there is a next page of result
    if response.ok:
        # get category page informations

        soup = BeautifulSoup(response.content, 'html.parser')
        h = soup.find_all('h3')

        # find if there is a next page
        next = soup.find('li', {'class': 'next'})

        # to create the url of all books
        for a in h:
            for link in a:
                links = link.get('href').replace('../../../', '')
                books_urls.append(url_book_path + links)

        # if next page exist
        if next:
            for link in next.find_all('a'):
                next_link = link.get('href')

                # create the next page url
                next_page = next_path + next_link
                get_books_links(next_page)



def get_category(url):

    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        ul = soup.find('ul', {'class': 'nav nav-list'}).find_all('a')

        for link in ul:
            links = link.get('href')
            category_url = category_path + links
            get_books_links(category_url)
            category_urls.append(category_url)



def get_a_book(url):
    """get book information"""

    # to read the doc and extract informations
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')

        # get the informations
        td = soup.find_all('td')
        p = soup.find_all('p')
        a = soup.ul.find_all('a')

        # transform book informations
        title = soup.h1.text
        product_description = p[3].text.replace(',', '.')
        upc = td[0].text
        price_excluding_tax = td[2].text
        price_including_tax = td[3].text
        number_available = td[5].text
        review_rating = td[6].text
        product_page_url = url
        image = soup.img['src'].replace('../../', '')
        image_url = url + image
        category = a[2].text

        csvfile = '{}.csv'.format(category)


        # load information on csvfile
        with open(csvfile, 'a', newline='', encoding='utf-8-sig') as books:

            bookswriter = csv.writer(books, delimiter=',', dialect='excel', quoting=csv.QUOTE_ALL)

            # to create the Headers of the csv file
            bookswriter.writerow(
                    ['product_page_url', 'universal_product_code',
                     'title', 'price_including_tax'
                        , 'price_excluding_tax', 'number_available',
                     'product_description', 'category',
                     'review_rating', 'image_url'])

            # write rows
            bookswriter.writerow([product_page_url, upc,
                                  title, price_including_tax,
                                  price_excluding_tax, number_available
                                  , product_description, category
                                  , review_rating, image_url])

get_category(url)


print(len(books_urls))
# to check if i have all 1000 books

