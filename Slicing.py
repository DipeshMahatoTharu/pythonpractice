# Extract a substring
# Write a Python program to extract the word "World" from the string:
# "hello world "


text = "Hello World"
print(text[6:11])

# Slice From the Start
# Given the string "Programming", write a program to print the first 6 characters

text="Programming"
print(text[0:6])

# Extract Middle Characters
# Given the string "Hello, Python!", extract the substring "Python" using slicing.

text="Hello Python!"
print(text[6:])

# Use Negative Indexing
# Write a program to extract the word "Code" from the string below using negative indexing:

text="learn to Code!"

print(text[-5:-1])

# Skip Characters
# Write a program to print every second character from the string "abcdefghi"

text="abcdefghi"
print(text[::2])

# Reverse the String
# Write a Python program to reverse the string "Palindrome" using slicing.

text="Palindrome"
print(text[::-1])


# Custom Range and Step
# Given the string "abcdefghij", write a program to print characters from index 1 to 8 with a step of 2.
text="abcdefghij"
# result=text[1:8:]
print(text[1:8:2])

# Dynamic Slicing
# Write a program that takes a string as input and slices out the first and last characters, then prints the remaining string.

num=input("enter a string: ")
print(num[1:-1])
