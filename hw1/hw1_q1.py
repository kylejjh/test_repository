'''
1. Display Fibonacci Series upto 10 terms

The Fibonacci series is a sequence where each number is the sum of the two preceding ones, starting with 0 and 1.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
'''

def fibonacci(n):
    fibonacci_series = [0, 1]
    for i in range(n - 2):
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series

print("Fibonacci Series (10 terms):", fibonacci(10))
