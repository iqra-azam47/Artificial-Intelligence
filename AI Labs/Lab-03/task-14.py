# Write a Python program to check the validity of password input by users.
#  Validation

# At least 1 letter between [a-z] and 1 letter between [A-Z].

# At least 1 number between [0-9].

# At least 1 character from [S#@].

# Minimum length 6 characters.

# Maximum length 16 characters.



import re
password=input("Enter your Password:")

if(6<= len(password)<=16 and
   re.search("[a-z]",password) and
   re.search("[A-Z]",password) and
   re.search("[0-9]",password) and
   re.search("[@$#]",password)):
    print("Valid Password")
else:
    print("Invalid Password")