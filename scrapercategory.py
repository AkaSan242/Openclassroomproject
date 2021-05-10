import requests
from bs4 import BeautifulSoup
import csv

books_url = [] #we'll use it to iterate on all category books
url = 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html' #category url
page_url = []
urlb = 'http://books.toscrape.com/catalogue/' #use to define the link that we use to get book infromation from book url


def get_category_books(url):
    #if there is one page
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        books_number = soup.form.strong.text
        category = soup.h1.text
        h = soup.find_all('h3') # to find all books urls


        for a in h:
            for link in a:
                links = link.get('href').replace('../../../', '') # to create the path with urlb
                title = link.get('title')
                books_url.append({title: urlb + links})

        #if there is more than one page
        for i in range(9):
            response = requests.get(url.replace('index.html', 'page-{}.html').format(str(i)))
            if response.ok:
                soup = BeautifulSoup(response.content, 'html.parser')
                books_number = soup.form.strong.text
                category = soup.h1.text
                page = soup.find('li', {'class':'current'}).text
                h = soup.find_all('h3')

                for a in h:
                    for link in a:
                        links = link.get('href').replace('../../../', '')
                        title = link.get('title')
                        books_url.append({title: urlb + links})


get_category_books(url)
print(books_url)













