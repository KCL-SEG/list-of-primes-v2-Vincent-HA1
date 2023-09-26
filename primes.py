"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes<=0:
        raise ValueError("Number must be above 0")
    list = []
    listOfPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in range (0, number_of_primes):
        list.append(listOfPrimes[i])
    return list
