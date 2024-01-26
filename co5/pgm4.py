# write a python program to read specific columns of a given CSV file and print the content of the columns.
import csv
with open("column.csv")as csv file:
 reader=csv.DictReader(csvfile)
print("name rollno program")
for row in reader:
 print(row['name']," ",row['rollno']," ", row['program'])