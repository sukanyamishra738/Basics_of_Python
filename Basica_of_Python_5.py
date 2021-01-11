# 1.Write a python program to get OS name,platfrom and release information
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())

# 2.Write a python program to locate python site-packages
import site
print(site.getsitepackages())

# 3.Write a python program to call an external command in python
import subprocess
return_code = subprocess.call(['ping','localhost'])
print("output of call():",return_code)

# 4.Write a python program to get the path and name of the file that is currently executing
import os
print("current file name: ",os.path.realpath(__file__))

# 5.Write a python program to find out the number of CPUs using.
import multiprocessing
print(multiprocessing.cpu_count())

# 6.Write a python program to parse a string to float or integer
n = "565.8977"
print(float(n))
print(int(float(n)))

# 7.Write a python program to get the current username
import getpass
print(getpass.getuser())

# 8.Write a python program to print without newline or space
for i in range(6):
    print(i,end = "")
print("\n")

# 9.Write a python program to determine profiling of python programs
import cProfile
def sum():
    print(1+2)
cProfile.run("sum()")
