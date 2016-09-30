#!/usr/bin/env python3

""" download_subs.py : movie information and download subtitles

Display file details, movie information from the OMDB API and download appropriate
subtitles in english and serbian language
"""

import io
import argparse
import json
from urllib.request import urlopen
import requests
from babelfish import Language
from subliminal import Video, download_best_subtitles, region, save_subtitles
from PIL import Image
from Spinner import Spinner

__author__ = "Miroslav Vidović"
__email__ = "vidovic.miroslav@yahoo.com"
__date__ = "30.09.2016."
__version__ = "0.1"
__status__ = "Development"

def get_args():
    """
    Get end parse the arguments with argparse

    """
    parser = argparse.ArgumentParser(description='Download subtitles for your movie.', \
        epilog="Script will download english and serbian subtitles for your video file. ")

    parser.add_argument('-f', '--file', help='Video file that needs subtitles', required=True)
    parser.add_argument('-d', '--download', help='Download the subtitles',
                        action="store_true", required=False)
    parser.add_argument('-i', '--info', help='Show OMDB info', action="store_true", required=False)

    # Print script version
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)

    # Parse the arguments
    args = parser.parse_args()

    # Extract individual variables from args
    file_path = args.file
    download_subs = args.download
    show_omdb_info = args.info

    return file_path, download_subs, show_omdb_info

def omdb_details(name, year):
    """
    Get the movie details using the ODMB API

    Print the details about the movie and the plot. Show the movie poster.

    :param name: name of the movie
    :type name: string
    :param year: movie release year
    :type year: string

    """

    name = name.replace(" ", "+")
    request = requests.get('http://www.omdbapi.com/?t=%s\
        &y=%s&plot=short&r=json' % (name, year))
    data = json.loads(request.text)
    print(json.dumps(data, indent=4, sort_keys=True))

    file_location = urlopen(data["Poster"])
    image_file = io.BytesIO(file_location.read())
    poster = Image.open(image_file)
    poster.show()

def short_details(video_file):
    """
    Short info

    Get some basic iformation about the movie and the video file.

    :param video_file: movie video file
    :type video file: subliminal Video object
    :returns: info about the movie and the file
    :rtype: string

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

    file_path, download_subs, show_omdb_info = get_args()
    video_file = Video.fromname(file_path)

    # Display the short info
    short_info = short_details(video_file)
    print(short_info)

    # If -i flag is set show the info from the omdb api
    if show_omdb_info is True:
        spinner = Spinner()
        spinner.start()
        omdb_details(video_file.title, video_file.year)
        spinner.stop()

    # If -d flag is set download the best matching subtitles
    if download_subs is True:
        spinner = Spinner()
        spinner.start()
        # Set the cache
        region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})
        # Download subtitles in serbian and english
        best_subtitles = download_best_subtitles([video_file], {Language('eng'),\
                        Language('srp')}, providers=None)
        spinner.stop()
        print(best_subtitles[video_file])
        best_subtitle_sr = best_subtitles[video_file][0]
        best_subtitle_en = best_subtitles[video_file][1]
        # Save the 2 subtitle files
        save_subtitles(video_file, [best_subtitle_sr])
        save_subtitles(video_file, [best_subtitle_en])

if __name__ == '__main__':
    main()
