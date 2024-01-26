# From a list of integers, create a list removing even numbers. 
n=int(input("Enter the limit:"))
list=[]
print("Enter the numbers:")
for i in range(n):
 a=int(input())
 list.append(a)
print("The list with even numbers is:",list)
for i in list:
 if(i%2==0):
  list.remove(i)
print("The new list is:",list)