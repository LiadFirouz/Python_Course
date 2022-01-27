# The program get a parameter of homework making the solution
# Parameters : """C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 8 - files\homework.txt"""
#              """C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 8 - files\solutions.txt"""


import sys
import os

ARGV_LENGTH = sys.argv.__len__() - 1
PATH = sys.argv[ARGV_LENGTH]


def is_two_parameters():
    """ Check if the script got only two parameters
        Returns: True / False"""

    if ARGV_LENGTH == 2:
        return True
    return False


def name_is_right(path1, path2):
    """ Check if the files names are correct
        Args: path1, path2 - the directory for the two files
        Returns: True / False"""

    if os.path.basename(path1) == 'homework.txt':
        if os.path.basename(path2) == 'solutions.txt':
            return True
    elif os.path.basename(path2) == 'homework.txt':
        if os.path.basename(path1) == 'solutions.txt':
            return True
    return False


def return_homework():
    """ Check which one is the homework file and which one is the solution
        Returns: 2 strs - homework_path and solution_path """

    if os.path.basename(PATH) == 'homework':
        return PATH, sys.argv[ARGV_LENGTH - 1]
    return sys.argv[ARGV_LENGTH - 1], PATH


def is_paths_exists():
    """ Check if the paths are exists
        Returns: True / False """

    if os.path.exists(PATH) and os.path.exists(sys.argv[ARGV_LENGTH - 1]):
        if name_is_right(PATH, sys.argv[ARGV_LENGTH - 1]):
            return True
    return False


def check_ex(split_line):
    """ Check if the line from homework is a math problem
        Args: split_line - list separated by space from txt file
        Returns: True / False """

    if len(split_line) == 3:
        if split_line[0].isdigit() and split_line[2].isdigit():
            if split_line[1] == '+' or split_line[1] == '-' or split_line[1] == '*' or split_line[1] == '/':
                return True
    return False


def calculator(split_line):
    """ Takes the list and do the math problem
        Args: split_line - list with two numbers and an operator
        Returns: int - the solution according tho the line """

    num1 = float(split_line[0])
    num2 = float(split_line[2])

    op = split_line[1]

    if op == '+':
        num1 = num1 + num2
    elif op == '-':
        num1 = num1 - num2
    elif op == '*':
        num1 = num1 * num2
    elif op == '/' and num2:
        num1 = num1 / num2

    if num1.is_integer():
        return int(num1)
    return num1


def main():
    if is_paths_exists():
        homework_path, solution_path = return_homework()

        'clear the solutions file'
        with open(solution_path, "r") as solutions:
            lines = solutions.readlines()
        with open(solution_path, "w") as solutions:
            for line in lines:
                solutions.write("")

        with open(solution_path, 'w') as solutions:
            with open(homework_path, 'r') as homework:
                for ex in homework:
                    split_line = ex.split()
                    if check_ex(split_line):
                        new_line = ex.strip() + ' = ' + str(calculator(split_line))
                        solutions.write(new_line + '\n')
                    else:
                        new_line = ex.strip() + " -can't solve, it need to be a math problem"
                        solutions.write(new_line + '\n')

    else:
        print('invalid parameters were insert!')


if __name__ == '__main__':
    main()
