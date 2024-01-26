# Generate Fibonacci series of N terms

t1=0
t2=1
next=t1+t2
n=int(input("Enter the limit:"))
print("The fibonacci series is:")
print(t1,"\n",t2)
for i in range(3,n+1):
 print(next)
 t1=t2;
 t2=next;
 next=t1+t2;