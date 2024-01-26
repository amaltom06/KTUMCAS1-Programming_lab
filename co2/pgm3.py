# Find the sum of all items in a list

l=[]
n=int(input("Enter the size of the list : "))
print("Enter elements : ")
for i in range(n):
 i=int(input())
 l.append(i)
print("Sum : ",sum(l))