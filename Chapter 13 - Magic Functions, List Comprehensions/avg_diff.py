def avg_diff(list1, list2):
    """The function returns the average difference between list1 and list2
        Args: list1, list2 - list
        Returns: int"""
    return (sum(list1) + sum(list2)) / (len(list1) + len(list2))


def main():
    print(avg_diff([1, 1, 1, 1], [1, 2, 3, 4]))


if __name__ == "__main__":
    main()