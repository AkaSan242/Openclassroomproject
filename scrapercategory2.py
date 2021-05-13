import requests
from bs4 import BeautifulSoup
import csv


books_url = []
#we'll use it to iterate on all category books links

url = 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'
#category url

next_path = 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/'
#use to create a path if there is a next page of result

url_book_path = 'http://books.toscrape.com/catalogue/'
#use to define the link of each book


def get_books_links(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        books_number = soup.form.strong.text
        h = soup.find_all('h3')
        next = soup.find('li', {'class': 'next'})

        #to create the link of the book
        for a in h:
            for link in a:
                links = link.get('href').replace('../../../', '')
                books_url.append(url_book_path + links)


        #if next page exist
        if next:
            for link in next.find_all('a'):
                next_link = link.get('href')
                next_page = next_path + next_link
                get_books_links(next_page)




get_books_links(url)

print(books_url)