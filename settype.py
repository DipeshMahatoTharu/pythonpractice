# Set Types (set, frozenset)

# set




# frozenset
# Create a frozenset with the same values as the numbers set.
# Try to add a value to the frozenset and observe what happens.

# Create a set numbers with the values {1, 2, 3, 4, 5}.
number ={1,2,3,4,5}
# Add 6 to the set and print it.

number.add(6)
print(number)
# Try to add a duplicate value to the set and print the result.
number.add(3)
print(number)

fronzenNumber=frozenset(number)

try:
    fronzenNumber.add(3)
    print(fronzenNumber)
except AttributeError as e:
    print("error",e)


