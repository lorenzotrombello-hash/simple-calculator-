import math as mt 

operator = input("choose an operator: (+ - * /)")
num1 = float(input("enter a number:"))
num2 = float(input("enter a number:"))

if "+" in operator:
    result = num1 + num2
    print(f"{round(result,2)}")

if "-" in operator:
    result = num1 - num2
    print(f"{round(result,2)}")

if "*" in operator:
    result = num1 * num2
    print(f"{round(result,2)}")

if "/" in operator:
    result = num1 / num2
    print(f"{round(result,2)}")