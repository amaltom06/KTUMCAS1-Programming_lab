# 1.write a python program to read a file line by line and store it in list. 

with open("stud.txt") as f:
 s_list=f.readlines()
 s_list=[x.strip() for x in s_list]
print("The content of the file are :")
print(s_list)