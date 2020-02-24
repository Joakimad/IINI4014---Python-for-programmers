# Write code that prints out the first 1000 prime numbers.
# The code must calculate the prime numbers; you are not allowed to use a table of pre-calculated primes.


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n - 1):
        if (n % i) == 0:
            return False
    return True


# for i in range(1000):
#     if is_prime(i):
#         print(i)

# Regner med det er noe feil med oppgaven her.
for i in range(7920):
    if is_prime(i):
        print(i)
