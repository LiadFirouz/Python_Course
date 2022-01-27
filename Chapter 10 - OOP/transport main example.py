NEW_YORK = (5, 5)
LONDON = (3, 3)
BERLIN = (2, 1)


def main():
    transport = __import__('transport class example')  # import file with space in name

    elal = transport.Plane()
    american_airlines = transport.Plane('american_airlines', NEW_YORK)
    british_airways = transport.Plane('british_airways', LONDON)
    lufthansa = transport.Plane('lufthansa', BERLIN)

    fleet = [elal, american_airlines, british_airways, lufthansa]
    for plane in fleet:
        print(plane)


if __name__ == "__main__":
    main()
