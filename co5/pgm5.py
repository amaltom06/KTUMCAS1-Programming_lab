import csv

fields = ['name', 'rollno', 'age']
sdict = [{'name': 'amal', 'rollno': 9, 'age': 22}, {'name': 'anurag', 'rollno': 16, 'age': 29}]

# Writing to CSV file
with open("dpt.csv", "w", newline='') as dfile:
    writer = csv.DictWriter(dfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(sdict)

# Reading and displaying CSV file contents without pandas
with open("dpt.csv", "r") as dfile:
    reader = csv.reader(dfile)
    for row in reader:
        print(row)