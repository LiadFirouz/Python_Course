# The program receives number from the user and checks if
# the number with five digits

# Output:
# the number itself
# each digit separately next to each other with comma
# summary of all digits

DIGITS_NUMBER = 5
STOP_THE_PROGRAM = 'EXIT'


def has_enough_digits(number):
    """ Check if the number has five digits
        Args: user_input - number
        Returns: True / False """
    count = 0
    while number != 0:
        number = int(number / 10)
        count += 1

    if count == DIGITS_NUMBER:
        return True
    return False


def each_digit(number):
    """ Separate the number into digits
        Args: user_input - a number with five digits
        Returns: List - with all the digits """

    digit_lst = []

    while number != 0:
        digit_lst.append(int(number % 10))
        number = int(number / 10)

    return digit_lst


def main():
    while True:
        user_input = input('Please insert your number: ')

        if user_input == STOP_THE_PROGRAM:
            break

        if user_input.isdigit():
            user_input = int(user_input)
            if has_enough_digits(user_input):
                print('The number is: ', user_input)

                list_of_digits = each_digit(user_input)
                digits_sum = 0
                for i in range(DIGITS_NUMBER - 1, 0, -1):
                    print(list_of_digits[i], end=", ")
                    digits_sum += list_of_digits[i]
                print(list_of_digits[0])

                print('summarize of all digits: ', list_of_digits[0] + digits_sum)



if __name__ == '__main__':
    main()
