# Write a Python program which accepts a sequence of comma separated
# 4 digit binary numbers as its input and print the numbers that are divisible
# by 5 in a comma separated sequence.


binary_numbers=input("Enter comma seperated 4-digit binary numbers").split(',')
result = [num for num in
binary_numbers if int(num,2) % 5 ==0]
print(",".join(result))