# List comprehensions:
# a. Generate positive list of numbers from a given list of integers

listnum=[2,-4,6,-10,22,34]
positivenum = [i for i in listnum if i>= 0]
print(positivenum)

# b. Square of N number

n=int(input("Enter the limit:"))
enlist=[i**2 for i in range(n+1)]
enlist


# c. Form a list of vowels selected from a given word

Word=(input("Enter a word:"))
v=[i for i in Word if i in 'aeiouAEIOU']
v


# d. List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

c=(input("Enter a character:"))
o=[ord(i) for i in c]
o
