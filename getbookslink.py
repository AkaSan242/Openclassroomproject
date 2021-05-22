"""Script de la fonction get_books_links"""
import requests
from bs4 import BeautifulSoup


def get_books_links(url, list):


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
                list.append(url_book_path + links)




        #if next page exist
        if next:

            for link in next.find_all('a'):
                next_link = link.get('href')

                for i in range(51):
                    next_path = 'http://books.toscrape.com/catalogue/category/books/{}_{}/'.format(category.lower().replace(' ', '-'), str(i))
                    # use to create a path if there is a next page of result                                                         #category index

                    next_page = next_path + next_link
                    #create next page url
                    get_books_links(next_page, list)


        else:
            print('il y a "{}" livres dans la catégorie "{}".'.format(books_number, category))





