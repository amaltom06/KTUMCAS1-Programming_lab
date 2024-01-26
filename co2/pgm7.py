# Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’ 
s=input("Enter any string:")
if s.endswith("ing"):
 print(s+"ly")
else:
 print(s+"ing")