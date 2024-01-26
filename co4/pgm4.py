# Create a class Time with private attributes hour, minute and second. Overload 
# ‘+’ operator to find sum of 2 time.

class Time:
 def __init__(self, hour=0, minute=0, second=0):
    self._hour = hour
    self._minute = minute
    self._second = second
 def __add__(self, other):
    total_seconds = self._hour * 3600 + self._minute * 60 + self._second + \
    other._hour * 3600 + other._minute * 60 + other._second
    new_hour, remainder = divmod(total_seconds, 3600)
    new_minute, new_second = divmod(remainder, 60)
    return Time(new_hour, new_minute, new_second)
 def __str__(self):
    return f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}"
a=int(input("Enter the hour of time1:"))
b=int(input("Enter the minute of time1:"))
c=int(input("Enter the second of time1:"))
x=int(input("Enter the hour of time2:"))
y=int(input("Enter the minute of time2:"))
z=int(input("Enter the second of time2:"))
time1 = Time(a,b,c)
time2 = Time(x,y,z)
sum_time = time1 + time2
print("Time 1:", time1)
print("Time 2:", time2)
print("Sum of Time 1 and Time 2:", sum_time)