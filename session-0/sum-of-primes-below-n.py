# Summation of primes below n

def sieve_of_eratosthenes(n):
    sum = 0
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1

    for i,is_prime in enumerate(primes):
        if is_prime:
            sum += i
    return sum

print(sieve_of_eratosthenes(2000000))

