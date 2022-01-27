print ("Please enter a string: ")
string = input()
char = string[0]
string = string[1:]
print(char + string.replace(string[1:], 'e'))

