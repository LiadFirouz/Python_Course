PATH = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 8 - files\Dear Prudence.txt"


def main():
    'write in file - a (append) '
    'NOTE: the changes happens only after closing the file'
    input_file = open(PATH, 'a')
    input_file.write('\nDear Prudence open up your eyes\n')
    input_file.close()

    'with open - close automatically the file after the with block'
    with open(PATH, 'r') as input_file:
        for line in input_file:
            print(line, end="")


if __name__ == '__main__':
    main()
