#Count the occurrences of each word in a line of text. 
str=input("Enter a sentence : ")
a=[]
a=str.split();
words=[a.count(i) for i in a]
print(dict(zip(a,words)))