# Display future leap years from current year to final year entered by user.
start=int(input("Enter the current year:"))
end=int(input("Enter the last year:"))
print("Upcoming leap years are:")
for year in range(start,end):
 if (year%4==0 and year%100!=0) or (year%400==0):
  print(year)