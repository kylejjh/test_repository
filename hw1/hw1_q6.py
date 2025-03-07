# 6.Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

def print_odd_even():
    for num in range(1, 21):
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

print_odd_even()
