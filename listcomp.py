# Write a list comprehension to create a new list containing only the even numbers from the list:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennum=[]

for i in numbers:
    if i % 2 == 0:
        evennum.append(i)

print(evennum)

#Given a list of names ["Alice", "Bob", "Charlie", "Diana"],
# create a new list containing only the names that start with the letter "C."

name =["Alice", "Bob", "Charlie", "Diana"]
name_start_with_c=[name for name in name if name.startswith("C")]
print(name_start_with_c)

# Create a list of squares for numbers from 1 to 10 using list comprehension.

squareNumbers=[x**2 for x in range(1,11)]
print(squareNumbers)

