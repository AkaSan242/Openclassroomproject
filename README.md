# Bookscrap

"Bookscrap" is an application who scrap the website 'http://books.toscrape.com/'

the point is to get informations about all the books inside (price, name, images..) and write them on csvfile for a data analysis.

## Installation

Things you have to do before execute the code:

Install Python =<3

Create a virtual environment by run `python -m venv env` in your work directory with the terminal

Activate the environment by run `source env/bin/activate`

Download requirements.txt and install the requires packages by run `pip install -r requirements.txt`

Download this 3 scripts:
                        
                        -booktoscrape.py
                        
                        -getbook.py
                        
                        -getbookslink.py
                        
Create a directory 'csvfiles' the csvfiles will be write inside
                        
Create a directory 'booksimages' like that all books images will not be mixed with csvfiles (to keep your directory clean, yes good directory matter lol don't thank me)

"by the way 'booksimages' is a convention i made you can choose another name but if you do open 'getbook.py' and change the name inside the fonction at the line
(wget.download(image_url, 'booksimages')."

                        
## Usage

To execute the application run `python bookstoscrape.py`

Step 1 the application will search all categories on the website and print the number of the all books for each category

Step 2 the application will create a csvfile for each category

Step 3 the application will get all books informations , write them on their category csvfile and download all books images to put them in the directory you've created for.

Final step now you have a csvfile for all books of each category and a directory with all images in your work directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.




