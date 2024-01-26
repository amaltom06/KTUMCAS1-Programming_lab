# Find biggest of 3 numbers entered. 
a=int(input("Enter num 1="))
b=int(input("Enter num 2="))
c=int(input("Enter num 3="))
if(a>b and a>c):
    print(a,"is greater")
elif(b>c and a>a):
    print(b,"is greater")
elif(c>a and c>b):
    print(c,"is greater")