# This is a Python implementation of Euclid's algorithm for GCD
# Practice for lecture 1 of COMP90038

def euclid_gcd(m, n: int):
    """Returns the greatest common divisor between inputs m, n"""
    while n != 0:
        r = m % n
        m = n
        n = r
    return m

m = 24
n = 8
print(euclid_gcd(m, n))
