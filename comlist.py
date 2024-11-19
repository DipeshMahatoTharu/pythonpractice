# Filter numbers divisible by 3:

# Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a new list containing only numbers divisible by 3.


number =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = [expression for item in iterable if condition]

CheckDivisibleby3=[x for x in number if x % 3 == 0]
print(CheckDivisibleby3)



        