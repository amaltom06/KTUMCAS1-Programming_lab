# Generate a list of four digit numbers in a given range with all their digits even and the
# number is a perfect square.
res=[]
for i in range(1000,9999):
 if all(int(x)%2==0 for x in str(i)):
  if int(i**0.5)**2==i:
   res.append(i)
print("List of numbers : ",res)