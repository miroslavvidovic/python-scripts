#!/usr/bin/env python3

"""
    garfield.py
Get the garfield comic by date
"""

import datetime
import io
import argparse
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get
from PIL import Image

def get_args():
    """
    Get the arguments with argparse

    :returns: day, month and year extracted from argparse
    :rtype: (integer, integer, integer)
    """
    parser = argparse.ArgumentParser(description='Get the beloved Garfield comic.', \
        epilog="The best way to keep track of Garfield. NOTE: 1st issue of Garfield \
        was on June 19th, 1978 ")

    # Available arguments
    parser.add_argument('-y', '--year', type=int, help='year the comic was published')
    parser.add_argument('-m', '--month', type=int, help='month the comic was published')
    parser.add_argument('-d', '--day', type=int, help='day the comic was published')

    # Print script version
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')

    # Parse the arguments
    args = parser.parse_args()

    # Extract the individual variables
    year = args.year
    month = args.month
    day = args.day

    # Check for empty vars
    if not all((year, month, day)):
        print("You need values for all 3 parameters: date, month and year.")
        sys.exit()

    return day, month, year


def check_date(year_entered, month_entered, day_entered):
    """
    Check if the date is valid

    Check if the entered date is valid and continue the script if it is valid,
    but if the date is not valid terminate the script.

    :param year_entered: year that will form the date
    :type year_entered: integer
    :param month_entered: month that will form the date
    :type month_entered: integer
    :param day_entered: day that will form the date
    :type day_entered: integer
    """
    try:
        datetime.date(year=year_entered, month=month_entered, day=day_entered)
    except ValueError:
        print("The date is not valid.")
        sys.exit()

def get_img_by_date(day, month, year):
    """
    Get the image by date

    Return the url of the Garfield comic image for the desired date.

    :param day: the day when the comic was published
    :param month: the month when the comic was published
    :param year: the year when the comic was published
    :returns: url of the comic
    :rtype: string
    """
    garfield_page = get("https://garfield.com/comic/%s/%s/%s" % (year, month, day))
    bsoup = BeautifulSoup(garfield_page.content, "lxml")
    status = garfield_page.status_code

    # Check the status code
    if status == 200:
        comic = bsoup.find('div', {'class': 'comic-display'})
        img = comic.find('img', {'class': 'img-responsive'})
        url = img.attrs['src']
        return url
    else:
        print("There is a " + str(status) + " error for the desired date.")
        sys.exit()

def main():
    """
    Main function

    Read the url and show the image.
    """
    day, month, year = get_args()
    print("The requested date is %i.%i.%i." % (day, month, year))
    check_date(year, month, day)
    url = get_img_by_date(day, month, year)
    print(url)
    file_location = urlopen(url)
    image_file = io.BytesIO(file_location.read())
    garfield_img = Image.open(image_file)
    garfield_img.show()

if __name__ == "__main__":
    main()
