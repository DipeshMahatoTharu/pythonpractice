# Write a program to loop through the string "Python" and print each character on a new line.

name="Python"
for x in name:
    print(name)

# Question: Modify the code to count and print the number of vowels (a, e, i, o, u) in the string "banana".

number = "banana"

vowelLetter=0
for char in number:
    if char  in 'aeiou':
        vowelLetter +=1
        print(char,end= " ")
print("\n The vowel letters are :", vowelLetter)


