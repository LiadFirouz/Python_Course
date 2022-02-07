def main():
    """
    Example: vector operations - returns the multiplied lists in one list
    list1 = [1, 2, -5, 6]
    list2 = [2, -1, 3, 4]
    #returns: [24, -15, 2, -2]
    print(set(map(lambda x, y: x * y, list1, list2))) """

    print(''.join((map(lambda x: x * 2, input("enter: ")))))


if __name__ == "__main__":
    main()
