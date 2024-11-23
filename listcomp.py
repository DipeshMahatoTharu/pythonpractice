# Write a list comprehension to create a new list containing only the even numbers from the list:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennum=[]

for i in numbers:
    if i % 2 == 0:
        evennum.append(i)

print(evennum)