# Write a Python program that accepts a sequence of lines
# (blank line to terminate) as input and prints the lines as output
# (all characters in lower case).


print ("Enter lines (press Enter on a blank line to stop):")
lines = []

while True:
    line=input()
    if line=="":
        break
    lines.append(line.lower())

print("\nOutput:")
for line in lines:
    print(line)