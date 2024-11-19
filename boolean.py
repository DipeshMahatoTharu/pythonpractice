# Basic Boolean Operations

# What are the two Boolean values in Python?
# Write a Python program to evaluate the following expressions and print their Boolean results:
# 10 > 5
# 15 == 20
# 8 < 3


print(10 > 5)
print(15 == 20)
print(8 < 3)



# What does Python return when you compare two values in an if statement?
# Write a Python program to compare two variables, a = 50 and b = 30, and print:
# "b is greater than a" if b > a
# "b is not greater than a" otherwise.

a = 50 
b = 30

if b>a:
    print(f"{b} is greater then a")
else:
    print(f"{a} is  greater then b")

# What does the bool() function do in Python?
# Write a Python program to evaluate the following values using bool() and print the results:
# "Hello"
# 0
# []
# 42


print(bool("Hello"))
print(bool(0))
print(bool([]))
print(bool(42))

# Write a Python program to create a class with a len()
# method that always returns 0. Create an object of this class and print its bool() value.

class Myclass():
    def __len__(self):
        return 0
    
Myclassobj=Myclass()
print(bool(Myclassobj))



# How can functions return Boolean values in Python?
# Write a Python program where a function checks if a number is even and returns True or False. 
# Use this function in an if statement to print:
# "Even number!" if the function returns True
# "Odd number!" otherwise.


def Check(num):
    return num % 2 == 0

number=int(input("Enter Number :"))

if Check(number):
    print("Number is even ")
else:
    print("number is odd")
    
        


