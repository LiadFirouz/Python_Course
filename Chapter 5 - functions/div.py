def div(number1, number2):
    """"return the divide of number1 and number2
        else returns - Illegal
        Args:
        number1 - integer
        number2 - integer"""
    if number1 != 0 or number2 != 0:
        return number1 / number2
    else:
        return "Illegal"


def main():
    number1 = input("please enter a number: ")
    if not number1.isnumeric():
        while not number1.isnumeric():
            number1 = input("insert a valid number:")
    number2 = input("please enter a number: ")
    if not number2.isnumeric():
        while not number2.isnumeric():
            number2 = input("insert a valid number:")
    if (div(int(number1), int(number2))) % 10 == 0:
        print(int(div(int(number1), int(number2))))
    print(div(int(number1), int(number2)))


if __name__ == "__main__":
    main()
