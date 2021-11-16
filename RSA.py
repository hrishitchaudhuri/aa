from random import *
import numpy as np
import math

def fermat_base2_test(n, k):
    '''
    Runs base2 primality test on n with k trials,
    returns 0 for composite, 1 for prime
    '''
    for i in range(k):
        a = randint(2, n-2)
        if pow(a,n-1,n) == 1:
            return 1
    return 0

def trial_division(n, trials):
    '''
    Trial Division Test
    '''
    for i in range(trials):
        check = randint(2,int(math.sqrt(n)))
        if n%check == 0:
            return False
    return True


def miiller_test_helper(d, n):
    a = 2 + randint(1, n - 4);
    x = pow(a, d, n);
    if (x == 1 or x == n - 1):
        return True;
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
    return False;

def miller_test( n, k):
    '''
    Miller Rabin primality test
    '''
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
    for i in range(k):
        if (miiller_test_helper(d, n) == False):
            return False;
    return True;
    

def generate_large_odd(bitlength):
    '''
        Randomly generate a binary string of given bit length (ending with 1 to make sure its odd)
        input: bit length
        output: odd number of given bit length
    '''
    n = '0b1'
    for i in range(bitlength-2):
        n += choice(['0','1'])
    n += '1'
    n=(int(n,2))
    return n


def generate_large_primes(bitlength):
    '''
        generates 2 large odd numbers of given bit length,
        runs fermat and M-R test and trial division for primality
        return 2 large primes of given bitlength
    '''
    num1=generate_large_odd(bitlength)
    num2=generate_large_odd(bitlength)
    
    while not(fermat_base2_test(num1,3) and miller_test(num1,4) and trial_division(num1,100)):
        num1=generate_large_odd(bitlength)
    while not(fermat_base2_test(num2,3) and miller_test(num2, 4) and trial_division(num2,100)):
        num2=generate_large_odd(bitlength)

    return num1,num2

def gcd(a, b):
   while a != 0:
      a, b = b % a, a
   return b

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
    p,q = generate_large_primes(size)
    n = p*q
    e = choice([2*i+1 for i in range(100)])

    while gcd(e, (p-1)*(q-1)) != 1:
        e = choice([2*i+1 for i in range(100)])
    
    d = find_mod_inverse(e,(p-1)*(q-1))
    pubkey = (e,n)
    privkey = (d,n)
    return {'public':pubkey,'private':privkey}

def __encrypt(block, e, n, keysize=128):
    '''
        keysize byte block encrypted/decrypted using pubkey/privkey
    '''
    c = b''
    blocknum = int.from_bytes(block, 'big')
    result = pow(blocknum, e, n).to_bytes(keysize,'big')
    for i in result:
        if i != 0:
            c += i.to_bytes(1,'big')
    return c


def encrypt(msg, e, n, keysize=128):
    '''
        Only pass bytes/bytearray as msg input

        msg: byte stream to be encrypted
        e, n: derived from public key
        returns cipher (bytestream) which is formed by c=(msg**e)mod n

        calls __encrypt by splitting msg bytestream into 8 byte blocks

        same function is called for decrypt as well (pass e = d for decryption)
    '''
    block_size = int((keysize/32)*8)
    pad_size = block_size - len(msg)%block_size

    if pad_size != 0:
        msg += b'\x00'*pad_size
    if len(msg) <= block_size:
        return __encrypt(msg, e, n, keysize=keysize)

    cipher = b''
    i = 0
    while i <= len(msg)-block_size:
        block = msg[i:i+block_size]
        cipher = cipher + __encrypt(block,e,n)
        i += block_size

    return cipher

