"""
garfield.py
"""
#!/usr/bin/env python3

import argparse
from bs4 import BeautifulSoup
from requests import get
from PIL import Image
from urllib.request import urlopen
import io

def get_img_by_date(day, month, year):
    garfield_page = get("https://garfield.com/comic/%s/%s/%s" % (year, month, day))
    bsoup = BeautifulSoup(garfield_page.content, "lxml")
    status = garfield_page.status_code

    if (status == 200):
        comic = bsoup.find('div', {'class': 'comic-display'})
        img = comic.find('img', {'class': 'img-responsive'})
        url = img.attrs['src']
        return (url)
    else :
        print("There is a " + str(status) + " error for the desired date.")
        quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get the beloved Garfield comic.',
         epilog="The best way to keep track of Garfield. NOTE: 1st issue of Garfield was on June 19th, 1978 ")

    # Available arguments
    parser.add_argument('-y', '--year', type=int, help='year the comic was published')
    parser.add_argument('-m', '--month', type=int, help='month the comic was published')
    parser.add_argument('-d', '--day', type=int, help='day the comic was published')

    # Print script version
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')

    # Parse the arguments
    args = parser.parse_args()

    url = get_img_by_date(args.day, args.month, args.year)
    print(url)
    fd = urlopen(url)
    image_file = io.BytesIO(fd.read())
    img = Image.open(image_file)
    img.show()
