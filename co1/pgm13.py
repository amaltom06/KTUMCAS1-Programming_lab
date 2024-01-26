#Accept an integer n and compute n+nn+nnn.
n=int(input("Enter a value to n:"))
sum=n+(n*11)+(n*111)
print(n,'+',(n*11),'+',(n*111),'=',sum)