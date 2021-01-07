# 1.write a python program to get the difference between a given number and 17,if the number is greater than 17 return double the absolute difference
# Twinkle, twinkle, little star,
# 	how i wonder what you are!
# 		Up above the world so high,
		# like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	how i wonder what you are!
print("Twinkle, twinkle, little star,\n\thow i wonder what you are!\n\t\tUp above the worldso high,\n\t\tlike a diamond in the sky.\nTwinkle, twinkle, little star,\n\thow i wonder what you are!")

# 2.write a python program to get the python version you are using
import sys
sys.version
sys.version_info

# 3.write a python program to display the current date and time
import datetime
s = datetime.datetime.now()
print(s.strftime("%Y/%m/%d %H:%M:%S"))

# 4.write a python program which accepts the radius of a circle from the user and compute the area
from math import pi
radius = float(input("enter the radius value:"))
area = pi * (radius**2)
print("area:",str(area))

# 5.write a python program which accepts the user's first and last name and print them in reverse order with a space between them.
first_name = input("First Name:")
last_name = input("Last Name:")
print("Hello" + " " + last_name + " " + first_name)

# 6.write a python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
num = int(input("enter the number:"))
diff = 17 - num
if num > 17:
    print(abs(diff)*2)
else:
    print(diff)
# 7.write a python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
n1 = int(input("1st num:"))
n2 = int(input("2nd num:"))
n3 = int(input("3rd num:"))
sum = n1+n2+n3
if n1==n2==n3:
    print(3*sum)
else:
    print(sum)
# 8.write a python program to get a new string from a given string where "Is" has been added to the front.If the given string already begins with "Is" then return the string unchanged
s = input("enter the string:")
if s[:2] == "Is":
    print(s)
else:
    print("Is" + s)
# 9.write a python program to find whether a given number(accept from the user) is even or odd, print out an appropriate message to the user
given_num = int(input("enter the num:"))
if given_num % 2 == 0:
    print("{} is an even number".format(given_num))
else:
    print("{} is an odd number".format(given_num))
# 10.write a python program to count the number 4 in a given list
list_1 = [1,2,3,4,5,4]
count = 0
for i in list_1:
    if i == 4:
        count +=1
print("the number of 4 in the list",count)

