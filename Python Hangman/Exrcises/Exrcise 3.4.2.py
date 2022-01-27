def replace_first_char_with_e():
    print ("Please enter a string: ")
    string = input()
    if(len(string)):
        first_char = string[0]
        string = string[1:]
        print(first_char + string.replace(first_char, 'e'))
    else:
        print("string is empty!")

replace_first_char_with_e()


