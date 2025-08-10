# src/hello.py
def is_prime(n: int) -> bool:
    if n < 2: return False
    if n % 2 == 0: return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True

low, high = 2, 10000
primes = [x for x in range(low, high+1) if is_prime(x)]
print("Count:", len(primes))
print("Sum:", sum(primes))
print("First 10:", primes[:10])
print("Last 10:", primes[-10:])
