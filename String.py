# Question: Write a program to find and print the length of the string "Hello, Dipesh!"

greeting = "Hello, Dipesh!"

check_length=len(greeting)

print("The length is :", check_length)

# Question: Write a function that takes a string as input and returns its length.
def askName():
    name=str(input("Enter your name :"))
    print("The length of user is :",len(name))

askName()

# Check String
# Question: Check if the word "Python" is present in the text "Python programming is fun." and print an appropriate message.



Text = "Python programming is fun."

if "Python" in Text:
    print("python is present")
else:    
    print("python is not present")
    
# Question: Modify the code to count how many times the word "free"
# # appears in the text "The best things in life are free! Free things are the best.".
TextFree="The best things in life are free! Free things are the best."

count=TextFree.lower().count("free")
print("The free is :",count)

# Check if NOT
# Question: Write a program to check if 
# the word "hard" is NOT in the string "Learning Python is fun!" and print "Easy to learn!" if true.
text="Learning Python is fun!"
if "hard" not in text:
    print("Easy to learn!")





# Question: Create a program that checks if the string "expensive" 
# is not present in "The best things in life are free!" and
# appends "affordable" to the string if true.
text="The best things in life are free!"
if "expensive" not in text:
    print("expensive not present")
    text +="affordable"
    print(text)
else:
    print("Expensive is present ")  
