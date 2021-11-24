'''RSA IMPLEMENTATION'''
import math
from random import randint, choice
from prime import *

class Keys():
    '''
    Key class
    '''
    def __init__(self, size):
        '''
        Generates RSA public and private keys of given bitlength
        '''
        p, q = generate_large_primes(size)
        n = p * q
        # print('n bits: ', n.bit_length())
        
        e = choice([2*i+1 for i in range(2**5)])

        while extended_gcd(e, (p - 1) * (q - 1))[0] != 1:
            e = choice([2*i + 1 for i in range(2**5)])
        d = pow(e, -1, (p - 1) * (q - 1))
        self.pub = e
        self.priv = d
        self.N = n

def generate_large_odd(bit_length):
    '''
        Randomly generate a binary string of given bit length (ending with 1 to make sure its odd)
        input: bit length
        output: odd number of given bit length
    '''
    num = ''
    for _ in range((bit_length // 2) - 1):
        num += choice(['0', '1'])
    num += '1'
    num = '0b' + num
    num = (int(num, 2))
    return num

def is_prime(num):
    if pseudoprime(num) and miller_rabin_primality_testing(num, 10):
        return True

def generate_large_primes(bitlength):
    '''
        generates 2 large odd numbers of given bit length,
        runs fermat and M-R test and trial division for primality
        return 2 large primes of given bitlength
    '''
    num1 = generate_large_odd(bitlength)
    num2 = generate_large_odd(bitlength)
    while not is_prime(num1):
        num1 = generate_large_odd(bitlength)
    while not is_prime(num2):
        num2 = generate_large_odd(bitlength)

    return max(num1, num2), min(num1, num2)


def gcd(first, second):
    while first != 0:
        first, second = second % first, first
    return second

def __encrypt(block: bytes, enc: int, N: int) -> bytes:
    '''
        keysize byte block encrypted/decrypted using pubkey/privkey
    '''
    blocknum = int.from_bytes(block, 'big')
    c = pow(blocknum, enc, N)
    # print("<", blocknum, c, ">")
    # res = c.to_bytes(math.ceil(c.bit_length() / 8), 'big')
    res = c.to_bytes(math.ceil(N.bit_length() / 8), 'big')
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
    block_size = 8
    # block_size = math.ceil(N.bit_length() / 8)

    if len(msg) <= block_size:
        return __encrypt(msg, enc, N)

    cipher = b''
    i = 0
    while i <= len(msg) - block_size:
        block = msg[i: i + block_size]
        cipher = cipher + __encrypt(block, enc, N)
        i += block_size
    cipher += __encrypt(msg[i:], enc, N)
    """
    res = b''
    for i in cipher:
        if i != 0:
            res += i.to_bytes(1, 'big')
    """
    return cipher

def __decrypt(block: bytes, enc: int, N: int) -> bytes:
    blocknum = int.from_bytes(block, 'big')
    c = pow(blocknum, enc, N)
    # print("<", blocknum, c, ">")
    # res = c.to_bytes(math.ceil(c.bit_length() / 8), 'big')
    res = c.to_bytes(8, 'big')
    return res

def decrypt(msg: bytes, dec: int, N: int) -> bytes:
    block_size = math.ceil(N.bit_length() / 8)

    if len(msg) <= block_size:
        return __decrypt(msg, dec, N)

    decipher = b''
    i = 0
    
    while i < len(msg) - block_size:
        block = msg[i: i + block_size]
        decipher = decipher + __decrypt(block, dec, N)
        i += block_size
    
    # decipher += __decrypt(msg[i:], dec, N)

    if i != len(msg):
        final_block = int.from_bytes(msg[i:], 'big')
        result = pow(final_block, dec, N)
        required_bytes = math.ceil(result.bit_length() / 8)
        # print(required_bytes)
        decipher += result.to_bytes(required_bytes, 'big')
    """
    res = b''
    for i in decipher:
        if i != 0:
            res += i.to_bytes(1, 'big')
    """
    return decipher