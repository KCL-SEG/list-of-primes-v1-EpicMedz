"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isNumPrime(number):
    if number == 2:
        return True
    else:
        for num in range(2, number):
            if (number % num) == 0:
                return False
        else:
            return True

def primes(number_of_primes):
    list = []
    count = 1
    numberToCheck = 2
    while count < number_of_primes + 1:
        if isNumPrime(numberToCheck):
            list.append(numberToCheck)
            count += 1
            numberToCheck += 1
        else:
            numberToCheck += 1
    print(f"{list}")
    return list

primes(20)
primes(1)
primes(2)