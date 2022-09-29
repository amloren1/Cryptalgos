"""
Exploring Diffie-Hellman key exchange.

For a generator, g which can generate all non-zero ....
and a prime number, p

Alice sends Bob: g ^ a % p
Bob sends Alice: g ^ b % p

Alice does not have the value of b however she can add the seecret she has, a
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

