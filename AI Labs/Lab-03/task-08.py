# 8. Write a Python program that prints all the numbers from 0 to 6 except
#  3 and 6.

# Note: Use 'continue' statement.
# Expected Output: 01245


for num in range(7):
    if num==3 or num==6:
      continue

    print(num,end="")
