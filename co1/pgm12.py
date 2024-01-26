# Create a list of colors from comma-separated color names entered by user. Display first and last colors.
n=int(input("Enter the no of colors you want to insert:"))
clist=[]
print("Enter the color:")
for i in range(n):
 color=input()
clist.append(color)
print(clist)
print("The first and last colors are:")
print(clist[0],clist[-1])