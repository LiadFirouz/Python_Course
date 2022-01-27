def main():
    for i in range(0, 101, 1):
        if (i % 7 == 0) or (int(i / 10) == 7) or (i % 10 == 7):
            print('BOOM', end=" ")
        else:
            print(i, end=" ")


if __name__ == '__main__':
    main()
    print("\n", 75 / 10)
