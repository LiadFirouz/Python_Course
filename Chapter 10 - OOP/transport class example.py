import random

CONTROL_TOWER_LOCATION = (4, 4)


class Plane:
    # Note: in python '__' represent hidden members like private in java
    # in that case y is changeable in main(), x can not be reach form the main()

    def __init__(self, name='default', airport=(0, 0)):
        """ For class plan there is two members: __x and y.
            __x - hidden member, isn't changeable in the main (unless dir())
            y - changeable member
            airport=(0, 0) - getting a new list or setting airport as default"""

        self.__x = airport[0]
        self.y = airport[1]
        self.name = name

    """ The functions: update_position get_position called methods"""

    def update_position(self):
        self.__x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

    """ Methods for getting members called accessor (getters) like: get_position"""

    def get_position(self):
        return self.__x, self.y

    """ Methods for changing members called mutators (setters) like: get_position"""

    def set_position(self, x, y):
        if (x, y) == CONTROL_TOWER_LOCATION:
            print("Location of the tower")
        elif x < 0 or y < 0:
            print("Illegal location")
        else:
            self.__x = x
            self.y = y
        print("Position set")

    def __str__(self):
        """ For printing an object you can to trample __str__ by making one"""

        return "{} in position: {}".format(self.name, self.get_position())


class Boat:
    def __init__(self):
        self.__x = 0
        self.__y = 0


def main():
    print("This main function is not reached if the file is imported")


if __name__ == "__main__":
    main()
