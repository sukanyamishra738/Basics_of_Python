# 1.write a python program to get the least common multiple(LCM) of two positive integers
def find_lcm(n1,n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    while(True):
        if greater%n1 == 0 and greater%n2 == 0:
            lcm = greater
            break
        else:
            greater += 1
    print("lcm:",lcm)
find_lcm(60,48)
find_lcm(10,15)

# 2.write a python program to sum of three given integers.However,if two values are equal sum will be zero.
def sum_of_3(x,y,z):
    if x == z or x == y:
        sum = 0
    else:
        sum = x+y+z
    print("sum of 3 numbers:",sum)
sum_of_3(1,2,3)

# 3.write a python program to sum of two given integers.However ,if the sum is between 15 to 20 it will return 20.
def sum_of_2(p,q):
    sum1 = p + q
    if sum1 >= 15 and sum1 <= 20:
        sum1 = 0
    print("sm of 2 numbers:",sum1)
sum_of_2(17,3)
sum_of_2(21,3)

# 4.write a python program that will return true if the two given integer values are equal or their sum or difference is 5.
def true_value(a,b):
    sum = a + b
    difference = a - b
    if a==b or sum == 5 or difference == 5:
        return True
    else:
        return False
print(true_value(5,5))
print(true_value(12,7))
print(true_value(2,3))
print(true_value(1,2))

# 5.write a python program to add two objects if both objects are an integer type.
def add_numbers(c,d):
    if (isinstance(c,int) and isinstance(d,int)):
        return c+d
    else:
        raise TypeError("Inputs must be integers")
print(add_numbers(3,4))
print(add_numbers(4,5))

# 5.write a pyrhon program to display your details like name ,age,address in three different lines
def display():
    name,age = "Anshuman", 24
    address = "Bangalore,India"
    print("Name:{}\nAge:{}\nAddress:{}".format(name,age,address))
display()

# 6.write a python program to solve (x+y)*(x+y).
def square(e,f):
    return (e+f)**2
print(square(4,3))

# 7.write a python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
def cal_SI(Pr,T,R):
    SI = (Pr*T*R) / 100
    return Pr+SI
print("the future value:",cal_SI(10000,7,3.5))

# 8.write a python program to compute the distance between the points(x1,y1) and (x2,y2)
import math
p1 = [4,0]
p2 = [6,6]
distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print(distance)

# 9.write a python program to check whether a file exists
from os import path
print("file exists:"+str(path.exists('guru99.txt')))

# 10.write a python program to determine if a python shell is executing in 32bit or 64bit mode on OS.
import struct
print(struct.calcsize("P")*8)