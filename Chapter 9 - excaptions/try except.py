# Parameter for exception - """C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 9 - excaptions\try except.txt"""
# Parameter for try - """C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 9 - excaptions"""

import sys
import os

PATH = 1

'try to show all the files in PATH'
try:
    directory = sys.argv[PATH]
    print(os.listdir(directory))

except IndexError:  # if there is any missing parameter print...
    print("Missing script parameter")
except WindowsError:  # if directory was not found print...
    print("No such directory")
except Exception as e:  # if their error which error print...
    print("Error: {}".format(e))
finally:  # the code in the block will continue although the exceptions
    print('end of code')