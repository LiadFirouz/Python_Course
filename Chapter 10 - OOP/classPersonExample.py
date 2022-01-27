class Person:
    def __init__(self, name='Shooki', age=20):
        self.__name = name
        self.__age = age

    def say(self):
        return "Hi :)"

    def __str__(self):
        return "Person {} is {} years old".format(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


def main():
    print('')


if __name__ == "__main__":
    main()
