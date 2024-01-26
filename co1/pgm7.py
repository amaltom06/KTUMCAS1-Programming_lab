# Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.
string = input("Enter any string:")
char=string[0]
string=string.replace(char, '$')
strmod=char + string[1:]
print(strmod)