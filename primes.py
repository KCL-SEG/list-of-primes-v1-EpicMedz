"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    for number in range(3, number_of_primes + 1):
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            list.append(number)
    print(f"{list}")
    return list