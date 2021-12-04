"""Class to generate keys."""
import random

import rsa
import prime

class Keys:
    """
    A class to define keys.
    """

    def __init__(self, size):
        """
        Generates RSA public and private keys of given bit-length.
        """
        prime_1, prime_2 = rsa.generate_large_primes(size)
        num = prime_1 * prime_2
        enc = random.choice([2**i + 1 for i in range(1, 32)])

        while prime.extended_gcd(enc, (prime_1 - 1) * (prime_2 - 1))[0] != 1:
            enc = random.choice([2*i + 1 for i in range(2**5)])
        dec = pow(enc, -1, (prime_1 - 1) * (prime_2 - 1))

        self.pub = (enc, num)
        self.priv = (dec, num)
