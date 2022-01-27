def main():
    number = input("please enter a number: ")
    print("you entered: ", number)
    print("the digits are: ", end=" ")
    sum = 0
    for i in number:
        print(i, end=", ")
        sum += int(i)
    print("\nthe sum: ", sum)


if __name__ == "__main__":
    main()