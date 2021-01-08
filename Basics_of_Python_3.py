# 1.write a python program to get a string which is n(non-negative integer) copies of a given string.
s = input("enter a string:")
new_string = ""
n = int(input("enter the number of times you want to copy:"))
for i in range(n):
    new_string = new_string + s + " "
print(new_string)

# 2.write a python program to get the n copies of the first 2 characters of a given string.Return the n copies of the whole string if the length is less than 2.
def string_copies(string,n):
    new_string_2 = " "
    if len(string) < 2:
        for i in range(n):
            new_string_2 = new_string_2 + string
    else:
        string2 = string[0] + string[1]
        for x in range(n):
            new_string_2 = new_string_2 + string2
    print(new_string_2)
string_copies("s",2)
string_copies("sweety",2)

# 3.write a python program to test whether a passed letter is a vowel or not.
def check_vowels(letter):
    all_vowels = "aeiouAEIOU"
    return letter in all_vowels
print(check_vowels("F"))

# 4.write a python program to check whether a specified value is contained in a group of values
def list_check(number):
    list_ = [1, 5, 8, 3]
    return number in list_
print(list_check(9))

# 5.write a python program to create a histogram from a given list of integers
def histogram(items):
    for n in items:
        output = ""
        while n > 0:
            output += "@"
            n = n-1
        print(output)
histogram([1,3,5,7])
# 6.write a python program to concatenate all elements in a list into a string and return it.
def str_concatenate(words):
    new_string_ = ""
    for word in words:
        new_string_ += str(word)
    print(new_string_)
str_concatenate([1,2,3,4])

# 7.write a python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
the_list = [386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,248,333,73]
def check_even(numbers):
    for i in numbers:
        if i == 237:
            break
        elif i%2 == 0:
            print(i)
check_even(the_list)
# 8.write a python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
color_list_1 = set(['white','Black','Red'])
color_list_2 = set(['Red','Green'])
print(color_list_1.difference(color_list_2))

# 9.write a python program that will accept the base and height of a triangle and compute the area.
base = float(input("enter the base:"))
height = float(input("enter the height:"))
area = 0.5*(base * height)
print("area of the triangle is:", area)
# 10.write a python program to compute the greatest common divisor(GCD) of two positive integers
def compute_gcd(w,z):
    if w>z:
        smaller = z
    else:
        smaller = w
    for p in range(1,smaller+1):
        if((w%p == 0) and (z%p == 0)):
            hcf = p
    return hcf
print("the HCF is:",compute_gcd(10,15))
# or
import math
print("the HCF is: ",end = "")
print(math.gcd(60,48))