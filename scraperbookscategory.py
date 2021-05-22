import requests
from bs4 import BeautifulSoup
import csv
import wget




books_urls = []
#we'll use it to iterate on all category books links

url = 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'
#category url



def get_books_links(url):

    url_book_path = 'http://books.toscrape.com/catalogue/'
    # use to define the link of each book

    response = requests.get(url)
    if response.ok:

        soup = BeautifulSoup(response.content, 'html.parser')
        books_number = soup.form.strong.text
        #number of books in the category

        category = soup.find('h1').text
        h = soup.find_all('h3')
        next = soup.find('li', {'class': 'next'})

        #to create the link of the book
        for a in h:
            for link in a:
                links = link.get('href').replace('../../../', '')
                books_urls.append(url_book_path + links)


        #if next page exist
        if next:

            for link in next.find_all('a'):
                next_link = link.get('href')
                next_path = 'http://books.toscrape.com/catalogue/category/books/{}_{}/'.format(category.lower().replace(' ', '-'), str(5))
                # use to create a path if there is a next page of result                                                         #page index

                next_page = next_path + next_link
                #create next page url
                get_books_links(next_page)
        else:
            print('il y a "{}" livres dans la catégorie "{}".'.format(books_number, category))


def get_a_book(url):
    """get book information"""

    url_i = 'http://books.toscrape.com/'

    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        #to read the doc and find the information

        #extract book informations
        td = soup.findAll('td')
        p = soup.findAll('p')
        a = soup.ul.find_all('a')

        #transform book informations
        title = soup.h1.text
        product_description = p[3].text.replace(',', '.')
        upc = td[0].text
        price_excluding_tax = td[2].text
        price_including_tax = td[3].text
        number_available = td[5].text
        review_rating = td[6].text
        product_page_url = url
        image = soup.img['src'].replace('../../', '')
        image_url = url_i + image
        wget.download(image_url, 'booksimages')
        category = a[2].text


        #load on csv file
        with open('onecategory.csv','a', newline='', encoding='utf-8-sig') as books:
            bookswriter = csv.writer(books, delimiter=',', dialect='excel')

            bookswriter.writerow([product_page_url, upc,
                                  title, price_including_tax,
                                  price_excluding_tax, number_available
                                     , product_description, category
                                     , review_rating, image_url])

        #to check the result while writing on csv
        print('livre: "{}", catégorie: "{}"'.format(title,category))


get_books_links(url)


#to compare with books numbers and check if we got all links
print('il y a "{}" livres dans books urls.'.format(len(books_urls)))


# load on csv file
with open('onecategory.csv', 'w', newline='', encoding='utf-8-sig') as books:
    bookswriter = csv.writer(books, delimiter=',', dialect='excel')

    # to create the Headers of the csv file
    bookswriter.writerow(
        ['product_page_url', 'universal_product_code',
         'title', 'price_including_tax'
            , 'price_excluding_tax', 'number_available',
         'product_description', 'category',
         'review_rating', 'image_url'])

#add books on csv file 'onecategory'
for url in books_urls:
    get_a_book(url)



