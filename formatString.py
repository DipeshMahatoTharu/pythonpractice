# Combining Strings and Numbers

# Why can't we combine strings and numbers directly using the + operator in Python?

# Rewrite the following code to fix the error using f-strings:
# python
# Copy code
# age = 25
# txt = "I am " + age + " years old"
# print(txt)

age = 25
txt = f"I am {age} years old"
print(txt)

# Using F-Strings

# What is an f-string, and when was it introduced in Python?
# Write a Python program to display the sentence: "My favorite number is 7" using an f-string with a variable.

x=7
print(f"My favourite number is {x}")
# print(txt)

# What does the modifier :.2f do when used in an f-string placeholder?
# Write a Python program to print "The discounted price is 12.50 dollars" when the price variable is 12.5

num=12.50
print(f"The discounted price is {num:.2f}   dollars")

# Placeholders with Python Code

# Can placeholders in f-strings contain Python code, such as math operations? Give an example.
# Write a Python program to calculate and display "3 items at $20 each is $60" using f-strings.

item,firstDollar,SecondDollar=3,20,60
Totalprice=firstDollar*item
print(f"The total cost for {item} items {firstDollar} at each is : {Totalprice} ")
