def half_lower_half_upper():
    print("please enter a string: ")
    string = input()
    firstHalf = string[:len(string)//2]
    secondHalf = string[len(string)//2:]
    print(firstHalf+secondHalf.upper())

half_lower_half_upper()