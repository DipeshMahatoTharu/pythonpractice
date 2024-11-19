# How can you loop through all items in a list using a for loop?
# Write a Python program to print each item in the list ["cat", "dog", "rabbit"] using a for loop.

list=["cat", "dog", "rabbit"]

for i in list:
    print(i)

# How can you loop through a list using its index numbers?
# Write a Python program to print the items of the list ["red", "green", "blue"] by referring to their index numbers.

indexList=["red", "green", "blue"]

for i in range(len(indexList)):
    print(indexList[i])
    
# Using a While Loop

# How can you loop through a list using a while loop?
# Write a Python program to print all the items in the list ["Monday", "Tuesday", "Wednesday"] using a while loop.

itemList=["Monday", "Tuesday", "Wednesday"]

indexnum=0

while indexnum<len(indexList):
    print(itemList[indexnum])
    indexnum +=1
    
    
# Using List Comprehension

# What is the shortest syntax for looping through all items in a list and performing an action on each item?
# Write a Python program to print all items in the list ["circle", "square", "triangle"] using list comprehension.
    
Geo=["circle", "square", "triangle"]

for i in Geo:
    print (i)

# Combining Looping and Conditions

# How can you use a loop to print only certain items from a list that satisfy a condition?


# Write a Python program to print only the items in the list ["apple", "banana", "cherry", "apricot"] that start with the letter "a".
listFruit=["apple", "banana", "cherry", "apricot"]

for i in listFruit:
    if i.startswith("a"):
        print(i)

# Write a Python program to create a new list where all items from 
# ["apple", "banana", "cherry"] are converted to uppercase using a loop

x= ["apple", "banana", "cherry"]


upperlist=[]

for i in x:
    upperlist.append(i.upper())

print(upperlist)



