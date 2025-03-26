#Task-09 Part 1

# Write a Python program to get the Fibonacci series between 0 to 50.
# Note: The Fibonacci Sequence is the series of numbers:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

# Every next number is found by adding up the two numbers before it.

# Expected Output: 1 1 2 3 5 8 13 21 34



a = 0
b = 1

while a<=50:
    print(a,end=" ")
    a , b = b , a + b



# Task-9 Part 2
# Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for the
# multiples of five print "Buzz". For numbers which are multiples of both
# three and five print "FizzBuzz".



for num in range(1,51):
    if num % 3 == 0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)
