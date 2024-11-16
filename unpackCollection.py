# Unpacking a Collection - Question:
# You have a list of colors:

# python

# colors = ["red", "green", "blue", "yellow"]
# Unpack the first three colors into the variables color1, color2, and color3.
# Unpack the remaining color(s) into a list named others.
# Print the values of color1, color2, color3, and others.

colors=["red","green","blue","yellow"]
colors1,colors2,colors3,*other=colors

print(colors1,colors2,colors3)
print([other])


# Create a list ["car", "bike", "bus", "train"].

# Unpack the first two into variables vehicle1 and vehicle2.
# Unpack the remaining into a list called other_vehicles.
# Print all variables.

vehicles=["cars","bike","bus","train"]
vehicles1,vehicles2, *other_vechicles=vehicles

print(vehicles1,vehicles2)
print(other_vechicles)

# Have a dictionary {"name": "Alice", "age": 25}.

# Unpack the keys into key1 and key2.
# Print the keys and their corresponding values

person={"name": "Alice","age":25}

key1,key2=person.keys()

valuue1=person[key1]
valuue2=person[key2]


print(f"{key1},{valuue1}")
print(f"{key2},{valuue2}")