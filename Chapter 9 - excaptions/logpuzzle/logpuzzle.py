#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
import operator
import os
import re
import sys
import webbrowser
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """ Returns a list of the puzzle urls from the given log file,
        extracting the hostname from the filename itself.
        Screens out duplicate urls and returns the urls sorted into
        increasing order."""

    # +++your code here+++
    url_filename = os.path.basename(filename)
    is_message = False

    if "logo" in url_filename:
        index = url_filename.find("logo_") + len("logo_")
    else:
        index = url_filename.find("message_") + len("message_")
        is_message = True

    url_server_name = url_filename[index:]
    url_list = []
    with open(filename, 'r+') as urls:
        for line in urls:
            get_index = line.find("GET") + len("GET ")
            jpg_index = line.find(".jpg ") + len(".jpg")
            if jpg_index > len(".jpg"):
                try:
                    urllib.request.urlopen('http://' + url_server_name + line[get_index:jpg_index])
                    url_list.append('http://' + url_server_name + line[get_index:jpg_index])
                except Exception as e:
                    print('error on {}'.format('http://' + url_server_name + line[get_index:jpg_index]))

    url_list = list(dict.fromkeys(url_list))

    if is_message:
        index = url_list[0].rfind('-') + 1
        return sorted(url_list, key=lambda x: x[index:])
    else:
        return sorted(url_list)



def download_images(img_urls, dest_dir):
    """ Given the urls already in the correct order, downloads
        each image into the given directory.
        Gives the images local filenames img0, img1, and so on.
        Creates an index.html in the directory
        with an img tag to show each local image file.
        Creates the directory if necessary."""

    # +++your code here+++
    # See if dest_dir exists--if not, create it
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)

    image_index = 0
    complete_html_image = ''
    for image_url in img_urls:
        try:
            with urllib.request.urlopen(image_url) as img_download:
                image = img_download.read()
                directory = dest_dir + "\img{}.jpg".format(image_index)
                complete_html_image += '<img src="{}">'.format(directory)
                image_index += 1

                with open(directory, 'wb') as output_file:
                    output_file.write(image)

            html_file = open(r'{}\index.html'.format(dest_dir), 'w+')
            html_file.write("<html>\n<body>\n{}\n</body>\n</html>".format(complete_html_image))
            html_file.close()
        except Exception as e:
            print('Error: {}'.format(e))
            print('Delete: {}'.format(img_urls.pop(input(image_url))))




def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 9 - excaptions\logpuzzle\images"
    if args[0] == '--todir':  # r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 9 - excaptions\logpuzzle"
        todir = args[1]
        del args[0:2]
    print(todir)
    img_urls = read_urls(args[0])

    if todir:
        print(img_urls)
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))

    print('Open solved puzzle...')
    webbrowser.open(r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 9 - excaptions\logpuzzle\images\index.html")


if __name__ == '__main__':
    main()
