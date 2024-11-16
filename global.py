# Declare a global variable status with the value "Active".
# Inside a function update_status(), use the global keyword to change the value of status to "Inactive".
# Call the update_status() function.
# Print the value of status after calling the function

status="Active"

def update_status():
    status="Inactive"
    print(status)


update_status()

print(status)

# Create a Global Variable Inside a Function:
# Write a Python program to:

# Define a function set_country() that creates a global variable country using the global keyword.
# Assign the value "Nepal" to country inside the function.
# Call the set_country() function and then print the value of the global variable country outside the function.

country=""
def set_county():
    global country 
    country="nepal"
    print(country)
    
set_county()
print(country)
    
