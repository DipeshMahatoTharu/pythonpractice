# Binary Types (bytes, bytearray, memoryview)
# bytes

# Create a bytes object from the string "hello" encoded in UTF-8.
# Print the bytes object.
bytObj=bytes("hello","UTF-8")
print(bytObj)


# bytearray
# Create a bytearray object from the bytes object and modify the first byte.
# Print the modified bytearray.

bytArry=bytearray(bytObj)
bytArry[0]=72
print("modified Array ", bytArry)



# memoryview
# Create a memoryview of the bytearray object and print its first byte.
memoryView=memoryview(bytArry)
print("Memorie view : ",memoryView[0])