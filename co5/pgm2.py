#write a program to copy odd lines of one file stud.txt to odd.txt and copy the even lines of the file to even.txt.

s=open("stud.txt","r")
o=open("odd.txt","w")
e=open("even.txt","w")
content=s.readlines()
content=[x.strip() for x in content]
print("The contents of the files are")
print(content)
for i in range(len(content)):
 if(i%2==0):
  e.write(content[i])
else:
  o.write(content[i])
s.close()
o.close()
e.close()