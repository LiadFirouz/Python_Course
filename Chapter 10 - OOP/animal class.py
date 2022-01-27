class Dog:
    def __init__(self, name='Doggo'):
        self.__name = name
        self.__age = 1

    def birthday(self):
        self.__age += 1

    def set_name(self, name):
        __name = name

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def __str__(self):
        return "{} is {} years old".format(self.get_name(), self.get_age())


def main():
    dog1 = Dog()
    print('name: {}\nage: {}'.format(dog1.name, dog1.age))
    dog1.birthday()
    print('name: {}\nage: {}'.format(dog1.name, dog1.age))


if __name__ == "__main__":
    main()
