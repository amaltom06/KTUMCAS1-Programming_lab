#write a python program to read each row from a given csv file and print a list of strings.

import csv
with open("class.csv","r") as file:
 data=csv.reader(file)
for i in data:
 print(i)