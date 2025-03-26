# Write a Python program which takes two digits m (row) and n (column)
# as input and generates a two-dimensional array. The element value in the 
# i-th row and j-th column of the array should be ij.


m = int(input("Enter number of rows:"))
n = int(input("Enter number of columns:"))

array = [[i*j for j in range(n)] for i in range(m)]
print(array)