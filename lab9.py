from kanren import isvar, run, membero
from kanren.core import success, fail, goaleval, condeseq, eq, var
from sympy.ntheory.generate import prime, isprime, primerange
import itertools as it
def check_prime(x):
    if isvar(x):
        return condeseq([(eq, x, p)] for p in map(prime, it.count(1)))
    else:
        return success if isprime(x) else fail
limit = int(input("Enter a limit to find primes up to: "))
prime_numbers_up_to_limit = list(primerange(1, limit + 1))
a = var()
result = set(run(0, a, (membero, a, prime_numbers_up_to_limit), (check_prime, a)))
print(f"Prime numbers up to {limit}: {result}")

"""
Enter a limit to find primes up to: 20
Prime numbers up to 20: {2, 3, 5, 7, 11, 13, 17, 19}
"""
