def main():

    #print((lambda x: x if x % 3 == 0 else None)(number)) print the number if it divides by 3
    #print(list(map(lambda n: n if n % 3 == 0 else None, range(0, n))))

    print(list(filter(lambda x: x % 3 == 0, range(1, int(input('enter a number: '))))))

if __name__ == "__main__":
    main()
