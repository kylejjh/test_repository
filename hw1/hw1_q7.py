# 7.Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.

def sum_of_integers(a,b):
    return a+b

num1 = input()
num2 = input()

result = sum_of_integers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")
