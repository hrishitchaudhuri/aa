'''RSA IMPLEMENTATION'''
from random import randint, choice
import math

class Keys():
    '''
    Key class
    '''
    def __init__(self, size):
        '''
        Generates RSA public and private keys of given bitlength
        '''
        p, q = generate_large_primes(size)
        n = p*q
        e = choice([2*i+1 for i in range(100)])

        while gcd(e, (p-1)*(q-1)) != 1:
            e = choice([2*i+1 for i in range(100)])
        d = find_mod_inverse(e, (p - 1) * (q - 1))
        self.pub = e
        self.priv = d
        self.N = n

def fermat_base2_test(num, trials):
    '''
    Runs base2 primality test on n with k trials,
    returns 0 for composite, 1 for prime
    '''
    for trial in range(trials):
        a = randint(2, num-2)
        if pow(a, num-1, num) != 1:
            return 0
    return 1


def trial_division(num, trials):
    '''
    Trial Division Test
    '''
    for trial in range(trials):
        check = randint(2, int(math.log(num)))
        if num % check == 0:
            return False
    return True


def miller_rabin_primality_testing(n, k):
    """Calculates whether n is composite (which is always correct) or prime
    (which theoretically is incorrect with error probability 4**-k), by
    applying Miller-Rabin primality testing.
    """
    # prevent potential infinite loop when d = 0
    if n < 2:
        return False

    # Decompose (n - 1) to write it as (2 ** r) * d
    # While d is even, divide it by 2 and increase the exponent.
    d = n - 1
    r = 0

    while not (d & 1):
        r += 1
        d >>= 1

    # Test k witnesses.
    for _ in range(k):
        # Generate random integer a, where 2 <= a <= (n - 2)
        a = randint(2, n - 3) + 1

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                # n is composite.
                return False
            if x == n - 1:
                # Exit inner loop and continue with next witness.
                break
        else:
            # If loop doesn't break, n is composite.
            return False

    return True


def generate_large_odd(bit_length):
    '''
        Randomly generate a binary string of given bit length (ending with 1 to make sure its odd)
        input: bit length
        output: odd number of given bit length
    '''
    num = '0b1'
    for i in range(bit_length - 2):
        num += choice(['0', '1'])
    num += '1'
    num = (int(num, 2))
    return num


def generate_large_primes(bitlength):
    '''
        generates 2 large odd numbers of given bit length,
        runs fermat and M-R test and trial division for primality
        return 2 large primes of given bitlength
    '''
    num1 = generate_large_odd(bitlength)
    num2 = generate_large_odd(bitlength)
    while not(fermat_base2_test(num1, 3) and miller_rabin_primality_testing(num1, 4) and trial_division(num1, 100)):
        num1 = generate_large_odd(bitlength)
    while not(fermat_base2_test(num2, 3) and miller_rabin_primality_testing(num2, 4) and trial_division(num2, 100)):
        num2 = generate_large_odd(bitlength)
    return num1, num2


def gcd(first, second):
    while first != 0:
        first, second = second % first, first
    return second


def find_mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def __encrypt(block: bytes, enc: int, N: int) -> bytes:
    '''
        keysize byte block encrypted/decrypted using pubkey/privkey
    '''
    cipher = b''
    blocknum = int.from_bytes(block, 'big')
    c = pow(blocknum, enc, N)
    res = c.to_bytes(len(block), 'big')
    return res



def encrypt(msg: bytes, enc: int, N: int) -> bytes:
    '''
        Only pass bytes/bytearray as msg input
        msg: byte stream to be encrypted
        e, n: derived from public key
        returns cipher (bytestream) which is formed by c=(msg**e)mod n
        calls __encrypt by splitting msg bytestream into 8 byte blocks
        same function is called for decrypt as well (pass e = d for decryption)
    '''
    block_size = int((N).bit_length() / 8)
    pad_size = block_size - (len(msg) % block_size)

    if pad_size != 0:
        msg += b'\x00' * pad_size

    if len(msg) <= block_size:
        return __encrypt(msg, enc, N)

    cipher = b''
    i = 0
    while i <= len(msg) - block_size:
        block = msg[i: i + block_size]
        cipher = cipher + __encrypt(block, enc, N)
        i += block_size
    return cipher
