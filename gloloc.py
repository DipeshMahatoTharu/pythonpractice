# Combine Local and Global Variables:
# Write a Python program to:

# Declare a global variable x with the value 100.
# Inside a function multiply_x(), create a local variable x with the value 10.
# Multiply the local x by 2 and print it inside the function.
# Print the global x outside the function.
# Expected Output:
# Inside the function: 20
# Outside the function: 100

x =100
def multiply_x():
    
    x=10*2
    print("Local Output :" ,x)

multiply_x()

print("global Value", x)

    

