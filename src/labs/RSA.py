"""
Implementing RSA

First step is to generate the keys:
1. Select two distinct prime numbers, p & q
2. Multiply them to receive a modulus, n
3. Compute the totient of n phi(n) = phi(p)*phi(q) = (p-1)*(q-1)
    Note: an update to RSA recommends using the Carmichael's totient
    function,lambda of n: 
            lambda(n) 
            = lcm(lambda(p), lambda(q)) 
            = lcm((p-1), q-1))
    The least common multiple of p,q may be calculated using the Euclidean algorithm:
    lcm(p,q) = abs(p * q) / gcd(p,q)
    where gcd is the greatest common denominator

    **lambda(n) is kept SECRET**

4 Select a prime number, e such that e is coprime to lambda(n)
    In other words, the greatest common denominator of e and lambda(n) is 1.

4. Find the modular inverse of e:
    d*e = phi(q) * phi(p) + 1

Where phi is Euler's totient function. It represents the count of numbers which are 
relatively prime (coprime) to the argument of the phi function. In other words phi(n) 
is the number of integers from 1 <= k <= n for which the greatest common 
divisor of n & k is equal to 1.
example:
phi(8)
  1 <- relatively prime
  2 common factors: 1, 2
  3 <- relatively prime
  4 common factors: 1, 2, 4
  5 <- relatively prime
  6 common factors: 1, 2
  7 <- relatively prime
  8 common factors: 1, 2, 4, 8
Therefore the phi of 8 is 4

The Carmichael function, lambda is also used is step 3. Where the lambda of a 
prime number is equivalent to the phi of a prime: 
    given a prime number, p:
        lambda(p) = phi(p) = p-1
Because we have n as the product of two primes, we can easily find the lambda of n
through the following relationship
    lambda(n) = lambda(p*q)
              = lcm(lambda(p), lambda(q)) <-least common multiple
              = lcm((p-1), (q-1))

More generally speaking, the Carmichael function will return the value m such that
    a^m % n = 1
so, lambda(n) = m

where, a is any number between 1 and n coprime with n. m being the 
smallest positive integer such that above holds true/
Example, find the lambda of 5
 n = 5
 a - [1, 2, 3, 4]
 m = 4
    1 ^ 4 % 5 = 1 
    2 ^ 4 % 5 = 1 
    3 ^ 4 % 5 = 1 
    4 ^ 4 % 5 = 1 

"""

import math
import random

def is_prime(p):

    for i in range(2, math.isqrt(p) +1):
        if p % i == 0:
            return False
    return True

def get_prime(n = 1000):

    while True:
        p = random.randrange(n , n*2)
        if is_prime(p):
            return p

def lcm(a, b):
    return a * b// math.gcd(a,b)

##
# Key generation. Done by Alice (secret) so that Bob can send message
##
# Step 1: Generate two distinct prime numbers
size = 300
p = get_prime(size)
q = get_prime(size)
print(f"Generate primes: {p}\t{q}")

# Step 2: compute modulus n = p * q
n = p*q
print(f"Modulus n: {n}")

# Step 3: Compute lambda(n), the least common multiple of lambda(p) and lambda(q)
lambda_n = lcm(p-1, q-1)
print(f"lambda n: {lambda_n}")

# Step 4