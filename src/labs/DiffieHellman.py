"""
Exploring Diffie-Hellman key exchange.

For a generator, g which can generate all non-zero ....
and a prime number, p

Alice sends Bob: g ^ a % p
Bob sends Alice: g ^ b % p

Alice does not have the value of b however she can add the secret she has, a
to what Bob sent her:
    (g ^ b % p) ^ a = (g ^ b) ^ a % p = g ^ ab % p

Bob can do the same with his secret, b.

Alice and Bob can then have the shared secret of 
    g ^ ab % p
    

The attacker on the other hand may have poached the the values exchanged
between Alice and Bob. Attacker Eve then has:

g ^ b % p    and
g ^ a % p

g and p are publicly available. a, b are the secrets. 
"""
import math
import random


def is_prime(p):

    for i in range(2, math.isqrt(p) + 1):
        if p % i == 0:
            return False
    return True


def get_prime(n=1000):

    while True:
        p = random.randrange(n, n * 2)
        if is_prime(p):
            return p


def is_generator(g, p):
    """
    Checks if g is a sufficient generator:

    generator should never go to 1
    """
    for i in range(1, p - 1):
        # if generator comes back to 1, the period restarts, period should be within p
        if (g**i) % p == 1:
            return False
    return True


def get_generator(p):
    """
    This is our primitive root in g ^ a % p

    Starts from our prime number, p
    """
    for g in range(2, p):
        if is_generator(g, p):
            return g


# finding the prime and generator
p = get_prime(10000)
g = get_generator(p)

print(f"\ngenerator: {g} \nmodulus: {p}")
# g, p up to this point are agreed upon publicly
# now Alice and Bob must select values from 0, p which will remain secret between them
# Alice: g ^ a % p
# Bob g ^ b % p

# Alice
a = random.randrange(0, p)
g_a = (g**a) % p

print(f"Alice: g_a = {g_a}")
# Bob
b = random.randrange(0, p)
g_b = (g**b) % p
print(f"Bob: g_b = {g_b}")

# Back to Alice
g_ab = (g_b**a) % p

# Back to Bob
g_ba = (g_a**b) % p

print(f"\nAlice Key = {g_ab:10}")
print(f"Bob Key = {g_ba:10}")
