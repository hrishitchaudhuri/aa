'''RSA IMPLEMENTATION'''
from random import randint, choice
import math


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
        check = randint(2, int(math.sqrt(num)))
        if num % check == 0:
            return False
    return True


def miiller_test_helper(d, num):
    a = 2 + randint(1, num - 4)
    temp = pow(a, d, num)
    if temp == 1 or temp == num - 1:
        return True
    while d != num - 1:
        temp = (temp * temp) % num
        d *= 2
        if temp == 1:
            return False
        if temp == num - 1:
            return True
    return False


def miller_test(num, trials):
    '''
    Miller Rabin primality test
    '''
    if num <= 1 or num == 4:
        return False
    if num <= 3:
        return True
    d = num - 1
    while d % 2 == 0:
        d //= 2
    for trial in range(trials):
        if miiller_test_helper(d, num) == False:
            return False
    return True


def generate_large_odd(bitlength):
    '''
        Randomly generate a binary string of given bit length (ending with 1 to make sure its odd)
        input: bit length
        output: odd number of given bit length
    '''
    num = '0b1'
    for i in range(bitlength - 2):
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
    while not(fermat_base2_test(num1, 3) and miller_test(num1, 4) and trial_division(num1, 100)):
        num1 = generate_large_odd(bitlength)
    while not(fermat_base2_test(num2, 3) and miller_test(num2, 4) and trial_division(num2, 100)):
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


def keygen(size):
    '''
    Generates RSA public and private keys of given bitlength
    '''
    p, q = generate_large_primes(size)
    n = p*q
    e = choice([2*i+1 for i in range(100)])

    while gcd(e, (p-1)*(q-1)) != 1:
        e = choice([2*i+1 for i in range(100)])
    d = find_mod_inverse(e, (p - 1) * (q - 1))

    pubkey = (e, n)
    privkey = (d, n)
    return {'public':pubkey, 'private':privkey}


def __encrypt(block, enc, N, keysize=128):
    '''
        keysize byte block encrypted/decrypted using pubkey/privkey
    '''
    cipher_block = b''
    blocknum = int.from_bytes(block, 'big')
    result = pow(blocknum, enc, N).to_bytes(keysize, 'big')

    for i in result:
        if i != 0:
            cipher_block += i.to_bytes(1, 'big')
    return cipher_block


def encrypt(msg, enc, N, keysize=128):
    '''
        Only pass bytes/bytearray as msg input

        msg: byte stream to be encrypted
        e, n: derived from public key
        returns cipher (bytestream) which is formed by c=(msg**e)mod n

        calls __encrypt by splitting msg bytestream into 8 byte blocks

        same function is called for decrypt as well (pass e = d for decryption)
    '''
    block_size = int((keysize/32)*8)
    pad_size = block_size - len(msg) % block_size

    if pad_size != 0:
        msg += b'\x00' * pad_size

    if len(msg) <= block_size:
        return __encrypt(msg, enc, N, keysize=keysize)

    cipher = b''
    i = 0
    while i <= len(msg) - block_size:
        block = msg[i: i + block_size]
        cipher = cipher + __encrypt(block, enc, N)
        i += block_size

    return cipher
