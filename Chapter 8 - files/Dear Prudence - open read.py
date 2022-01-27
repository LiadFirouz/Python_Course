PATH = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 8 - files\Dear Prudence.txt"


def main():
    'opening a new file - r (read), w (write)'
    input_file = open(PATH, 'r')

    ':type - shows the type of the object'
    print(type(input_file))

    'reading the file all at once'
    'NOTE: not effective on big files - big pressure on the memory slower the reading'
    lyrics = input_file.read()
    #print(lyrics)

    'reading line by line'
    'NOTE: the last line of the file will be - " '
    lyrics = input_file.readline()

    'printing all the file using .readline()'
    input_file = open(PATH, 'r')
    lyrics = None
    while lyrics != '':
        lyrics = input_file.readline()
        #print(lyrics, end="")

    '.readline() - shorten way:'
    input_file = open(PATH, 'r')
    for line in input_file:
        print(line, end="")
    input_file.close()


if __name__ == '__main__':
    main()
