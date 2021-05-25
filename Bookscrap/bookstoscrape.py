from getbook import get_a_book
from getbookslink import get_books_links
from getcategory import get_category

"""Script to scrape the website 'books.toscrape.com'"""

url = 'http://books.toscrape.com/index.html'
#website url

category_urls = []
#to keep the categories urls on a list and use them to find all books urls

books_urls = []
#use to get books informations and write them on a csvfile for each category


get_category(url, category_urls)
#get all category links and create a csvfile for each category

del category_urls[0]
#we dont need the main page

for url in category_urls:
    get_books_links(url, books_urls)
#Get all books link in one category

for url in books_urls:
    get_a_book(url)
#get book informations and write them in his category csvfile

print('il y a "{}" livres sur le site Bookstoscrape et "{}" catégories'.format(len(books_urls), len(category_urls)))
# to check if i have all 1000 books



