def main():
    i =  6 #int(input('Enter a number: '))
    f = lambda x: x + 2
    print(f(i))

    #sort by absolut
    print(sorted([2, -8, 5, -6, -1, 3], key=lambda x: x if x > 0 else x * -1))


if __name__ == "__main__":
    main()
