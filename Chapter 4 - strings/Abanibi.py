def abanibi(str):
    end = 0
    if 'a' in str or 'e' in str or 'i' in str or 'o' in str or 'u' in str:
        while end < len(str):
            if 'a' == str[end] or 'e' == str[end] or 'i' == str[end] or 'o' == str[end] or 'u' == str[end]:
                str = str[:end] + str[end] + "b" + str[end:]
                end += 2

            end += 1

    return str


def main():
    user_input = input("Please enter something: ")
    user_input = abanibi(user_input)
    print(user_input)


if __name__ == '__main__':
    main()
