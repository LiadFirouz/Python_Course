def last(str):
    return str[-1]


def main():
    'sort by the last char'
    beatels = ['John', 'Paul', 'George', 'Ringo']
    beatels.sort(key=last)
    print(beatels)

    'sort by the length of the words'
    beatels.sort(key=len)
    print(beatels)

    'sort by reverse'
    beatels.sort(reverse=False)
    print(beatels)
    beatels.sort(reverse=True)
    print(beatels)

if __name__ == '__main__':
    main()
