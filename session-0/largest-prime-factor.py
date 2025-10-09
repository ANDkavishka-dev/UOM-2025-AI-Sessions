n = 600851475143
p = 2
while p * p <= n:
    if n % p == 0:
        n //= p
    else:
        p += 1
print(n)
