# The program receives two path (parameters - homework.txt, solutions.txt)
# the program will solve all the math exercises in order to the solutions.txt
# e.g: '49 +  2' ---> '49 + 2 = 51'
# the format of the exercise must be: 'number-space-operator-space-number'
# else print a custom error why

# Parameters: "C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 9 - excaptions\solutions.txt"
#             "C:\Users\LiadF\OneDrive\PythonNetwork\Python\Chapter 9 - excaptions\homework.txt"

import sys
import os

PATH = 1


def set_paths(dir1, dir2):
    """ Set the path into the right variable
        Args: dir1, dir2 - 2 str (path)
        Returns: path,path """
    if os.path.basename(dir1) == 'homework.txt':
        if os.path.basename(dir2) == 'solutions.txt':
            return dir1, dir2

    elif os.path.basename(dir2) == 'homework.txt':
        if os.path.basename(dir1) == 'solutions.txt':
            return dir2, dir1


def is_op(s):
    """ Gets str and check if it's an operator
            Arg: s - str
            Returns: True / False"""

    if len(s) == 1:
        if s == '+' or s == '-' or s == '*' or s == '/':
            return True
    return False


def check_line_format(line):
    """ Gets a line from a file and check if it in the right format,
        the format is: number-space-operator-space-number
        Arg: line - str
        Returns: True / False"""

    split_line = line.split()
    if len(split_line) == 3:
        if split_line[0].isdigit() and split_line[2].isdigit() and is_op(split_line[1]):
            return True
    return False


def calculator(line):
    split_line = line.split()

    num1 = int(split_line[0])
    op = split_line[1]
    num2 = int(split_line[2])
    try:
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 / num2

    except ZeroDivisionError:
        print('Error : cannot divide by zero')


def main():
    try:
        homework_directory = sys.argv[PATH]
        solutions_directory = sys.argv[PATH + 1]

        homework_directory, solutions_directory = set_paths(homework_directory, solutions_directory)

        with open(homework_directory, 'r') as homework:
            with open(solutions_directory, 'w') as solutions:
                for line in homework:
                    if check_line_format(line):
                        new_line = line.strip() + " = {}".format(str(calculator(line)))
                        solutions.write(new_line + '\n')
                        # solve
                    else:
                        new_line = line.strip() + " - can't solve, it's need to be a math exercise"
                        solutions.write(new_line + '\n')



    except IndexError:  # if there is any missing parameter print...
        print("Missing script parameter")
    except TypeError:  # if there is any missing parameter print...
        if os.path.isfile(homework_directory):
            print("Error : {} - No such a file".format(solutions_directory))
        else:
            print("Error : {} - No such a file".format(homework_directory))
    except Exception as e:  # if their error which error print...
        print("Error: {}".format(e))


if __name__ == '__main__':
    main()
