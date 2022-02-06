def anti_bi(s):
    """The function returns the average difference between list1 and list2
        Args: list1, list2 - list
        Returns: int"""
    return s.replace('b', '')


def main():
    print(anti_bi('the bee buzz all day long'))


if __name__ == "__main__":
    main()