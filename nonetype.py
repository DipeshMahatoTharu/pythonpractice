# None Type (NoneType)
# Create a variable x and assign it the value None.
x=None

# Check if x is None using the is keyword and print the result.
print("Is x none?", x is None)

# Write a function that doesn’t return any value, call it, and check its return type.
def noReturnvalue():
    pass

check=noReturnvalue()
print("The type is :", type(check))