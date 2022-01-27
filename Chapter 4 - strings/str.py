def find_word(word, str):
    start = 0
    end = 0
    for i in range(len(str)):
        if word[0] == str[i]:
            start = i
            end = len(word) + i
            if word == str[start:end]:
                return start, end


def main():
    str = 'Hello, my name is lnigo Montoya'

    start, end = find_word("Hello", str)
    print(str[start:end])

    start, end = find_word("my name", str)
    print(str[start:end])

    print(str[::2])

    print(str[2:19:2])
  

if __name__ == '__main__':
    main()
