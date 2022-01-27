def mul(number1, number2):
    """"return  the multiply of number1 and number2
    Args:
        number1 - integer
        number2 - integer"""
    return number1 * number2


def main():
    number1 = input("please enter a number: ")
    if not number1.isnumeric():
        while not number1.isnumeric():
            number1 = input("insert a valid number:")
    number2 = input("please enter a number: ")
    if not number2.isnumeric():
        while not number2.isnumeric():
            number2 = input("insert a valid number:")
    print (mul(int(number1), int(number2)))


if __name__ == "__main__":
    main()
