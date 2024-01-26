# Merge two dictionaries.
dict1={}
n=int(input("Enter the no.of items in the dictionary:"))
for i in range(n):
 key=input("Enter key: ")
value=input("Enter value: ")
dict1[key]=value
print(dict1)
dict2={}
m=int(input("Enter the no.of items in the dictionary:"))
for i in range(m):
 key=input("Enter key: ")
value=input("Enter value: ")
dict2[key]=value
print(dict2)
print(dict1|dict2)