# Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
n=int(input("Enter the number of elements:"))
list=[]
print("Enter the numbers")
for i in range (n):
 a=int(input())
 if(a<100):
  list.append(a)
 else:
  list.append('over')
print(list)