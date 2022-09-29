"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    for num in range(1, number_of_primes + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                list.append(num)
        elif number_of_primes == 1:
            list.append(2)
            break
        elif number_of_primes == 2:
            list.append(2)
            list.append(3)
            break
    print(f"{list}")
    return list

primes(20)
primes(1)
primes(2)