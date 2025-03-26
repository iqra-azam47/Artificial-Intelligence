# Task 3
# 3. Write a Python program to guess a number between 1 to 9.
# Note: User is prompted to enter a guess. If the user guesses wrong then 
# the prompt appears again until the guess is correct, on successful guess,
# user will get a "Well guessed!" message, and the program will exit.


import random
x=random.randint(1,9)

choice=int(input("Enter guess between 1-9:"))

while(choice!=x):
    choice=input("Invalid guess,Enter Again:")



print("You entered valid guess that is:",choice)

