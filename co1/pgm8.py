# Create a string from given string where first and last characters exchanged.
word=input("enter a word")
s=word[-1]+word[1:-1]+word[0]
print(s)