# The program moves the text from the filed text to the empty one
# e.g: A ---> B  or  B ---> A

A_PATH = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 8 - files\A.txt"
B_PATH = r"C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 8 - files\B.txt"


def not_wroten():
    """ Checks the which one of the file is empty
        Returns: str - the empty path """
    with open(A_PATH, 'r') as input_file:
        first_char = input_file.read(1)
        if not first_char:
            return A_PATH
    return B_PATH


def main():
    filed_file = A_PATH
    empty_file = not_wroten()

    if empty_file == A_PATH:
        filed_file = B_PATH

    'moving the information from one to another'
    input_file = open(empty_file, 'a')
    with open(filed_file, 'r+') as output_file:
        for line in output_file:
            input_file.write(line)
            output_file.write("")
        input_file.close()

    'deleting the filed file'
    with open(filed_file, "r") as fp:
        lines = fp.readlines()
    with open(filed_file, "w") as fp:
        for line in lines:
            fp.write("")


if __name__ == '__main__':
    main()
