# Create a single string separated with space from two strings by swapping the character at position 1. 
s1=input("Enter the first string : ")
s2=input("Enter the second string : ")
s3=s2[0]+s1[1:]+" "+s1[0]+s2[1:]
print("Swapped string is :",s3)