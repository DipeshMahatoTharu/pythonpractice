# Type Conversion Questions
# Convert the following:
# 10 (integer) to float
# 20.5 (float) to integer
# 15 (integer) to complex number
# Write the program to perform these conversions and display the results.

x=10

con=float(x)

print(con)

y = 10

num=int(y)
print(num)

z=15
result=complex(z)
print(result)

print(type(result))

# What will happen if you try to convert a complex number to another type in Python? Explain with an example.

complenum= 10+11j
convertToInt=int(complenum)
print("Conversion",convertToInt)
