"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    list.append(2)
    for number in range(2, number_of_primes):
        for num in range(2,number):
            if number % num == 0:
                break
            elif number not in list:
                list.append(number)
    print(f"{list}")
    return list




primes(10)
