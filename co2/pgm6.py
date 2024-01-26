#  Count the number of characters (character frequency) in a string. 
string = input("Enter a string: ")
char_count = {}
for char in string:
 char_count[char] = char_count.get(char, 0) + 1
for char, count in char_count.items():
 print(f"'{char}': {count}")