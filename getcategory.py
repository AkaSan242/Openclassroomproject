import requests
from bs4 import BeautifulSoup
import csv


def get_category(url, list):

    category_path = 'http://books.toscrape.com/'
    # use to create the link for a category url

    #to extract the link of all categories
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        ul = soup.find('ul', {'class': 'nav nav-list'}).find_all('a')

        for link in ul:
            links = link.get('href')
            category_url = category_path + links
            list.append(category_url)

        #create csvfile for all categories
        for i in range(len(ul)):
            with open('csvfiles/{}.csv'.format(ul[i].text.strip()), 'w', newline='', encoding='utf-8-sig') as books:
                bookswriter = csv.writer(books, delimiter=',', dialect='excel', quoting=csv.QUOTE_ALL)

                # to create the Headers of the csv file
                bookswriter.writerow(
                        ['product_page_url', 'universal_product_code',
                         'title', 'price_including_tax'
                            , 'price_excluding_tax', 'number_available',
                         'product_description', 'category',
                         'review_rating', 'image_url'])