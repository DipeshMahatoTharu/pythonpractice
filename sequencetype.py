# Sequence Types (list, tuple, range)
# list
# Create a list fruits with the values ["apple", "banana", "cherry"].
# Add "orange" to the list and print it.
# Remove "banana" from the list and print it.

# tuple
# Create a tuple colors with the values ("red", "green", "blue").
# Print the second element of the tuple.
# Try to change the first element of the tuple and observe what happens.

# range
# Create a range of numbers from 1 to 10 and print all the numbers.
# Use a range to print only the even numbers from 1 to 10.

fruits =["apple","banana","cherry"]

fruits.append("orange")

print("Printing fruit after adding oranges",fruits)

fruits.remove("banana")
print("After removing the banana ", fruits)

colors=["red", "green", "blue"]
print("The second elementy for tuple is :",colors[1])

try:
    colors[0]="yellow"
    print(colors)
except TypeError as e:
    print("error",e)