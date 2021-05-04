import requests
from bs4 import BeautifulSoup
import csv


book_url = 'http://books.toscrape.com/catalogue/forever-and-forever-the-courtship-of-henry-longfellow-and-fanny-appleton_894/index.html'
url = 'http://books.toscrape.com/' #use to get the image_url in the fonction (get_a_book)


def get_a_book(book_url):
    """get book information"""
    response = requests.get(book_url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser') #to read the doc and find the information
        td = soup.findAll('td')
        p = soup.findAll('p')

        title = {'title': soup.h1.text}
        product_description = {'description':p[3].text}
        upc = {'upc': td[0].text}
        price_excluding_tax = {'price(excl.tax)':td[2].text}
        price_including_tax = {'price(incl.tax}':td[3].text}        #book information
        number_available = {'available':td[5].text}
        review_rating = {'review':td[6].text}
        product_page_url = {'url':book_url}
        image = soup.img['src'].replace('../../', '')
        image_url = {'image url': url + image}
        a = soup.ul.find_all('a')
        category = {'category':a[2].text}


    with open('books.csv', 'w', newline='', encoding='utf-8-sig') as books:  #write the info on a csvfile

        fieldnames = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(books, fieldnames=fieldnames, dialect='excel')
        
        writer.writeheader()
        
        writer.writerow({'product_page_url':product_page_url, 'universal_product_code':upc, 'title':title, 'price_including_tax':price_including_tax,'price_excluding_tax':price_excluding_tax,'number_available':number_available ,'product_description':product_description,'category':category,'review_rating':review_rating,'image_url':image_url})

bookscraper = get_a_book(book_url)

