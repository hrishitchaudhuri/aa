"""Core functions for RSA cryptosystem"""
import math
import random

import prime

def generate_large_odd(bit_length):
    """
    Randomly generate an odd binary string of given bit length.
    """
    num = ''
    for _ in range((bit_length // 2) - 1):
        num += random.choice(['0', '1'])
    num += '1'
    num = '0b' + num
    num = (int(num, 2))
    return num

def is_prime(num):
    """
    Run primality tests on given number.
    """
    if prime.pseudoprime(num) and prime.miller_rabin_primality_testing(num, 10):
        return True
    return False

def generate_large_primes(bitlength):
    """
    Randomly generate two odd numbers of given bit length.
    """
    num1 = generate_large_odd(bitlength)
    num2 = generate_large_odd(bitlength)

    while not is_prime(num1):
        num1 = generate_large_odd(bitlength)
    while not is_prime(num2):
        num2 = generate_large_odd(bitlength)

    return max(num1, num2), min(num1, num2)

def __encrypt(block, enc, num):
    """
    Encrypt message of given block-size using given key.
    """
    blocknum = int.from_bytes(block, 'big', signed=False)
    if blocknum > num:
        raise OverflowError()
    cipher = pow(blocknum, enc, num)

    res = cipher.to_bytes(math.ceil(num.bit_length() / 8), 'big')
    return res

def encrypt(msg, enc, num):
    """
    Encrypt message of variable block-size using RSA cryptography.
    """
    block_size = 8

    if len(msg) <= block_size:
        return __encrypt(msg, enc, num)

    cipher = b''
    i = 0
    while i <= len(msg) - block_size:
        block = msg[i: i + block_size]
        cipher = cipher + __encrypt(block, enc, num)
        i += block_size
    cipher += __encrypt(msg[i:], enc, num)
    return cipher

def __decrypt(block, enc, num):
    """
    Decrypt message of given block-size using given key.
    """
    blocknum = int.from_bytes(block, 'big')
    cipher = pow(blocknum, enc, num)
    res = cipher.to_bytes(8, 'big')
    return res

def decrypt(msg, dec, num):
    """
    Encrypt message of variable block-size using RSA cryptography.
    """
    block_size = math.ceil(num.bit_length() / 8)

    if len(msg) <= block_size:
        return __decrypt(msg, dec, num)

    decipher = b''
    i = 0

    while i < len(msg) - block_size:
        block = msg[i: i + block_size]
        decipher = decipher + __decrypt(block, dec, num)
        i += block_size

    if i != len(msg):
        final_block = int.from_bytes(msg[i:], 'big')
        result = pow(final_block, dec, num)
        required_bytes = math.ceil(result.bit_length() / 8)
        decipher += result.to_bytes(required_bytes, 'big')

    return decipher
