# Task-02
# Write a Python program to convert temperatures to and from 
# Celsius, Fahrenheit. [

# Formula: c/5=f-32/9 [where c = temperature in Celsius and f = temperature in
# Fahrenheit]



def celsius_to_faren(celsius):
    return(celsius*9/5)+32

def faren_to_celsius(faren):
    return(faren-32)*5/9

choice=input("Enter C if you want to covert into celsius and F to convert in Farenheit: ")
if choice=='C':
    celsius=float(input("Enter temperature in Celsius:"))
    print(celsius,"Celsius is eual to",celsius_to_faren(celsius),"F")

if choice=='F':
    faren=float(input("Enter temperature in farenheit:"))
    print(faren,"Farenheit is eual to",faren_to_celsius(faren),"C")

if choice!='C' and choice!='F':
    print("Invalid Choice!")