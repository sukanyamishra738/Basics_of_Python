# 1.write a python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
inputs = input("your input here:" )
lists = inputs.split(",")
print(lists)
tuples = tuple(lists)
print(tuples)

# 2.write a python program to accept a filename from the user and print the extension of that
filename = input("input the filename:")
extensions = filename.split(".")
print("the file extension is",extensions[-1])

# 3.write a python program to display the first and last colors from the following list
color_list = ["Red","Green","White","Black"]
first_color = color_list[0]
last_color = color_list[-1]
print("first_color:",first_color)
print("last color:",last_color)

# 4.write a python program to display the examination schedule.(extract the date from exam_st_date)
exam_st_date = (11,12,2014)
print("exam date is:" + str(exam_st_date[0])+"/"+str(exam_st_date[1])+"/"+str(exam_st_date[2]))
# or
print("exam date is:%i/%i/%i"%exam_st_date)

# 5.write a python program that accepts an integer(n) and computes the value of n+nn+nnn.
n = int(input("your input here:"))
n1 = int("%i"%n)
n2 = int("%i%i"%(n,n))
n3 = int("%i%i%i"%(n,n,n))
value = n1+n2+n3
print("the value of n+nn+nnn:",str(value))

# 6.write a python program to print the documents(syntax,description etc.)of python built-in function(s).
print(abs.__doc__)
print(list.__doc__)

# 7.write a program to print the calender of a given month and year.
import calendar
y = int(input("input the year:"))
m = int(input("input the month:"))
print(calendar.month(y,m))

# 8.write a python program to print the following here document
print("""
a string that you "don't" have to escape 
This
is a .......multi-line
heredoc string --------> example
""")

# 9.write a python program to calculate number of days between two dates
from datetime import date
dt1 = date(2014,7,2)
dt2 = date(2014,7,11)
difference = dt2 - dt1
print("The number of days between date1 and date2:",difference.days)

# 10.write a python program to get the volume of a sphere with radius 6
from math import pi
voulme = 4/3*(pi*6**3)
print("the volume of sphere with radius 6:",voulme)