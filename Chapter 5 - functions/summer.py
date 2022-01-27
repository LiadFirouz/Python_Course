def summer(lst):
    result = 0
    if isinstance(lst[0], int):
        for i in range(0, len(lst)):
            result += lst[i]

    elif isinstance(lst[0], bool):
        for i in range(0, len(lst)):
            if lst[i]:
                result += 1

    elif isinstance(lst[0], str):
        for i in range(0, len(lst)):
            if i == 0:
                result = lst[0]
            else:
                result = result + lst[i]

    elif isinstance(lst[0], list):
        for i in range(0, len(lst)):
            if i == 0:
                result = lst[0]
            else:
                result = result + lst[i]
    return result


def main():

    print(summer([10, 11, 12, 0.75]))
    print(summer([True, False, True, True]))
    print(summer(['aa', 'bb', 'cc']))
    print(summer([[1, 2, 3, 'a'], [4, 'b', 'c', 'd']]))


if __name__ == "__main__":
    main()
