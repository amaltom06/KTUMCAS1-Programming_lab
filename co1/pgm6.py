# Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums
# to same value (c) whether any value occur in both

n1=int(input("Enter the limit of first list:"))
list1=[]
print("Enter the elements:")
for i in range(n1):
 a1=int(input())
list1.append(a1)
n2=int(input("Enter the limit of second list:"))
list2=[]
print("Enter the elements:")
for i in range(n2):
 a2=int(input())
list2.append(a2)
print("The first list is",list1)
print("The second list is",list2)
if len(list1) == len(list2):
   print("The number of elements in list 1 and List 2 are EQUAL=",len(list1),"," ,len(list2))
else:
   print("The number of elementsin list 1 and List 2 are NOT EQUAL=",len(list1),"," ,len(list2))
if sum(list1)==sum(list2):
   print("Sum of List 1 and List 2 are EQUAL",sum(list1), "and",sum(list2))
else:
   print("Sum of List 1 and List 2 are NOT EQUAL",sum(list1), "and",sum(list2))
check = any(item in list1 for item in list2)
if check is True:
   print("Yes, Same value occur in both")