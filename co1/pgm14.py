# Print out all colors from color-list1 not contained in color-list2. 
n=int(input("Enter the no of colors you want to insert:"))
clist=[]
print("Enter the color:")
for i in range(n):
 color=input()
clist.append(color)
print(clist)
print("The first and last colors are:")
print(clist[0],clist[-1])