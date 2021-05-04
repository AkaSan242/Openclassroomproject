import requests
from bs4 import BeautifulSoup
import csv


url = 'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/page-1.html'
urlb = 'http://books.toscrape.com/catalogue/'



response = requests.get(url)
if response.ok:

    soup = BeautifulSoup(response.content, 'html.parser')
    books_number = soup.form.strong.text
    category = soup.h1.text
    h = soup.find_all('h3')
    for a in h :
        for link in a:
            links = link.get('href').replace('../../../', '')
            title = link.get('title')
            print({title:urlb + links})



