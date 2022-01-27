def mul_2nums(num1, num2):
    if num1 < 0 or num2 < 2:
        return 0

    return num1 * num2


def beep(str):
    return str + 'beep'


def main():
    str = input("Enter a number: ")
    print(beep(str))

    num1 = input('enter first number: ')
    num2 = input('enter second number: ')
    print(mul_2nums(int(num1), int(num2)))


if __name__ == "__main__":
    main()
