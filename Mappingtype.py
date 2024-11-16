# Mapping Type (dict)
# Create a dictionary student with keys "name", "age", and "grade", and assign them appropriate values.




student={"name":"Asiya","age":21,"grade":"kindergarten"}

key1,key2,key3=student.keys()

value1=student[key1]
value2=student[key2]
value3=student[key3]

print(f"{key1}:{value1}")
print(f"{key2}:{value2}")
print(f"{key3}:{value3}")

# Print the value of the "name" key.
print("the value of sudent name is :",student["name"])

# Add a new key "address" and assign it a value.
student["address"]="Kamalpokhari"
print("adding student address : ",student["address"])

# Remove the "grade" key from the dictionary and print the result.
del student["grade"]
print("printing after deleting the grade : ",student)

