string = (input("enter a string: "))
string = string.lower().replace(" ", "")
backword_string = string[::-1]

if(string == backword_string):
    print("OK")
else:
    print("NOT")


