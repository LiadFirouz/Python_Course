def main():
    for i in range(1, 51, 1):
        if (i % 10) == 0:
            print(int(i / 10), "\n")
        else:
            print(i / 10, end=" ")


if __name__ == '__main__':
    main()
