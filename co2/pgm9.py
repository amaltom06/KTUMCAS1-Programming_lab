#  Construct following pattern using nested loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *

n = int(input("Enter number of rows: "))
for i in range(n):
 for j in range(i):
  print ('* ', end="")
print('')
for i in range(n,0,-1):
 for j in range(i):
  print('* ', end="")
print('')