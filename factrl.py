#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if len(sys.argv) != 2:
    print("Usage: python factorial.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)

if num < 0:
    print("Error: Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
