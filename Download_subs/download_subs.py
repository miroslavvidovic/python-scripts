#!/usr/bin/env python3

""" download_subs.py : short descripton of what the script does

Longer description
"""

import os
import io
import argparse
import requests
import json
from urllib.request import urlopen
from babelfish import *
from subliminal import *
from PIL import Image
from Spinner import Spinner

__author__ = "Miroslav Vidović"
__email__ = "vidovic.miroslav@yahoo.com"
__date__ = "30.09.2016."
__version__ = "0.1"
__status__ = "Development"

def get_args():
    """
    Get the arguments with argparse

    """
    parser = argparse.ArgumentParser(description='Download subtitles for your movie.', \
        epilog="Script will download english and serbian subtitles for your video file. ")

    parser.add_argument('-f','--file', help='Video file that needs subtitles', required=True)
    parser.add_argument('-d','--download', help='Download the subtitles', action="store_true", required=False)
    parser.add_argument('-i','--info', help='Show IMDB info', action="store_true", required=False)

    # Print script version
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)

    # Parse the arguments
    args = parser.parse_args()

    file_path = args.file
    download_subs = args.download
    show_imdb_info = args.info

    return file_path, download_subs, show_imdb_info

def omdb_details(name, year):
    """
    Get the movie details using the ODMB API

    """
    #TODO: Format the movie name with word+word and then use it in the get request
    request = requests.get('http://www.omdbapi.com/?t=We+still+kill+the+old+way&y=2014&plot=short&r=json')
    data = json.loads(request.text)
    print (json.dumps(data, indent=4, sort_keys=True))

    file_location = urlopen(data["Poster"])
    print(file_location)
    image_file = io.BytesIO(file_location.read())
    poster = Image.open(image_file)
    poster.show()

def short_details(video_file):
    """
    Print short info

    Print the movie title, year and some basic info about the file.

    :param video_file:
    :returns:
    :rtype:

    """

    data = {'title': video_file.title, 'year': video_file.year, 'format': video_file.format,\
            'group': video_file.release_group, 'resolution': video_file.resolution, \
            'age': video_file.age}

    video_details = """
    Movie details
    -------------------
    Title: {title}
    Year:  {year}

    File details
    -------------------
    Released by: {group}
    Format:      {format}
    Resolution:  {resolution}
    File age:    {age}
    """

    return video_details.format(**data)

def main():
    """
    Main function

    """

    file_path, download_subs, show_imdb_info = get_args()
    video_file = Video.fromname(file_path)

    short_info = short_details(video_file)
    print(short_info)

    if download_subs == True:
      spinner = Spinner()
      spinner.start()

      region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})
      best_subtitles = download_best_subtitles([video_file], {Language('eng'), Language('srp')}, providers=None)
      spinner.stop()

      print(best_subtitles[video_file])
      best_subtitle_sr = best_subtitles[video_file][0]
      best_subtitle_en = best_subtitles[video_file][1]
      save_subtitles(video_file, [best_subtitle_sr])
      save_subtitles(video_file, [best_subtitle_en])

if __name__ == '__main__':
    main()
