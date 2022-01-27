import urllib11
import sys
import os
from urllib.parse import urlparse

URL = "https://assets-global.website-files.com/6005fac27a49a9cd477afb63/600755c0f6e8528535a4569d_snowflake-after.jpg"
FILENAME = urlparse(URL)
FILE = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 9 - excaptions\{}".format(os.path.basename(FILENAME.path))

def main():
    with urllib.request.urlopen(URL) as response:
        image = response.read()
    with open(FILE, 'wb') as output_file:
        output_file.write(image)
    print('he')


if __name__ == '__main__':
    main()
