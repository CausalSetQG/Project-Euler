""" Project Euler Problem 31:
In the United Kingdom the currency is made up of pound (£) and pence (p). 
There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
# Initialize a list to store the number of ways to make change for each possible amount from 0 to 200
ways = [0]*201

# There's one way to make change for the amount 0 (i.e., by not using any coins)
ways[0] = 1

# Iterate over each coin denomination
for x in [1,2,5,10,20,50,100,200]:
    # For each coin denomination, update the 'ways' list based on previously computed values
    for i in range(x, 201):
        # If the current amount 'i' can be formed using the coin denomination 'x',
        # add the number of ways to make change for the amount 'i-x' to 'ways[i]'
        ways[i] += ways[i-x]
    # Print the updated 'ways' list for debugging purposes
    print(ways)

# Print the number of ways to make change for the target amount 200
print(ways[200])
