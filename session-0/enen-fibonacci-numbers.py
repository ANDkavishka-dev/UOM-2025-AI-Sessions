a, b = 1, 2
total = 0
while b <= 4_000_000:
    if b % 2 == 0:
        total += b
    a, b = b, a + b
print(total)

