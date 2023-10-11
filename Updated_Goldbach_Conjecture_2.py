""" PROJECT EULER PROBLEM 46:
It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

\[
9 = 7 + 2 \times 1^2\\
15 = 7 + 2 \times 2^2\\
21 = 3 + 2 \times 3^2\\
25 = 7 + 2 \times 3^2\\
27 = 19 + 2 \times 2^2\\
33 = 31 + 2 \times 1^2
\]

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime 
and twice a square?
"""

from math import *

# Maximum value for the test
test = 6000

# Function to generate prime numbers up to a given maximum
def primes(maximum):
    list = []
    # Create a list of numbers from 3 to the given maximum
    for i in range(3, maximum):
        list.append(i)
    # Initialize a list with the first prime number, 2
    primes = [2]
    # Loop through the list of numbers and identify prime numbers
    for i in list:
        prime = 1
        for j in primes:
            if i % j == 0:
                prime = 0
        if prime == 1:
            primes.append(i)
    return primes

# Function to generate squares up to the square root of a given maximum
def squares(maximum):
    squares = []
    for num in range(1, int(sqrt(maximum))):
        squares.append(num**2)
    return squares

# Generate a list of squares and prime numbers up to the given test value
s = squares(test)
p = primes(test)

# Generate a list of odd numbers up to the test value
odds = range(3, test, 2)
# Initialize an empty list to store odd composite numbers
oddcomp = []
# Loop through the list of odd numbers and identify odd composite numbers
for num in odds:
    if num not in p:
        oddcomp.append(num)

# Check each odd composite number to see if it can be written as the sum of a prime number and twice a square
for num in oddcomp:
    true = 0
    for prime in p:
        for square in s:
            if prime + 2 * square == num:
                true += 1
    # If an odd composite number cannot be written in this way, print that number
    if true == 0:
        print(num)
        break
