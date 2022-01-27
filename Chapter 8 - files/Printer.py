# The program get a parameter while running
# Parameters : """C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 8 - files"""

import sys
import os

NAME = 1
PATH = sys.argv[NAME]


def main():

    if os.path.isdir(PATH):
        print(os.listdir(PATH))
    else:
        print('Directory not found')

if __name__ == '__main__':
    main()
