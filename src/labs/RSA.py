"""
Implementing RSA

First step is to generate the keys:
1. Select two distinct prime numbers, p & q
2. Multiply them to receive a modulus, n
3 Select a prime number, e such that e is not a factor of n
4. Find the modular inverse of e:
    d*e = phi(q) * phi(p) + 1

Where phi is Euler's totient function. It represents the count of numbers which are 
relatively prime to the argument of the phi function. In other words phi(n) 
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

"""