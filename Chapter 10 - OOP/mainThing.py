from classBigThing import BigThing
from classBigCat import BigCat


def main():
    my_thing = BigThing(5)
    print(my_thing.size())

    latif = BigCat('latif', 22)
    print(latif.size())


if __name__ == "__main__":
    main()
