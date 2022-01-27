def fibonacci(f1, f2):
    if (f1 + f2) <= 10000:
        f1, f2 = f2, (f1 + f2)
        print(f2, end=" ")
        fibonacci(f1, f2)


def main():
    fibonacci(0, 1)


if __name__ == '__main__':
    main()
