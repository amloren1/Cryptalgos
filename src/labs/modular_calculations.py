# generator modular 7 which produces all non-zero elements in the modulus
# so 1,2,3,4,5,6 must all be generated

"""
A generator g generates all the non-zero elements in the modulus. Hence, a generator g modulus 7 will generate the elements 1, 2, 3, 4, 5, 6 (but not in that order).

Find the first smallest generator modular 7.

For the power of i 0, 1, 2, .., 6 write the value of the generator to the power of i modular 7

The value 1 should be printed as the first and last output to the screen
"""
g = 3
for i in range(7):
    print(g**i % 7)
