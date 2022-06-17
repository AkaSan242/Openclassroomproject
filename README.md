# Bookscrap

"Bookscrap" is an application who scrap the website 'http://books.toscrape.com/'

the point is to get informations about all the books inside (price, name, images..) and write them on csvfile for a data analysis.

## Installation

Things you have to do before execute the code:

Install Python =<3

Create a virtual environment by run `python -m venv env` in your work directory with the terminal

Activate the environment by run `source env/bin/activate`

Download :

          -bookscrap.py
          -bookscraplib.py
          -requirements.txt
          

Install the requires packages by run `pip install -r requirements.txt`
                        
Create a directory 'csvfiles' the csvfiles will be write inside
                        
Create a directory 'booksimages' like that all books images will not be mixed with csvfiles (to keep your directory clean, yes good directory matter lol don't thank me)

"by the way 'booksimages' is a convention i made you can choose another name but if you do open 'getbook.py' and change the name inside the function at the line
(wget.download(image_url, 'booksimages/')."

                        
## Usage

To execute the application run `python bookstoscrape.py`

Step 1 the application will search all categories on the website and print the number of the all books for each category

Step 2 the application will create a csvfile for each category and put them on your 'csvfiles' directory

Step 3 the application will get all books informations , write them on their category csvfile and download all books images to put them in the directory you've created for(booksimages).

Final step now you have a csvfile for all books of each category and a directory with all images in your work directory.

## Contribution

[Luc Aka-Evy
](https://github.com/Luc-Aka-Evy)

## More

You can use 'Bookscrap' for just one book or just one category too if you want you just have to download the script made for.

For the one book version go on the website copy the url of the book you want and paste it on the script 'bookscrapbook.py' in 

url = 'yourbookurl'

Same thing if you take the category version copy the link in 'bookscrapcategory.py'

The installation is the same the difference is if you use the one book version you have to run `python scraperbook.py` 
and `python scraperbookscategory.py` if you use the category version.

ps: if you take the three version please make sure to make a directory for each one (i guess it's obvious but maybe not for everyone).






