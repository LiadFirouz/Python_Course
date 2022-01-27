
def main():
    animal = __import__('animal class')
    dog = animal.Dog('Yoni')
    print(dog)
    dog.birthday()
    print(dog)


if __name__ == '__main__':
    main()
