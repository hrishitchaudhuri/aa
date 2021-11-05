from random import *
import numpy as np

def fermat_base2_test(n):
    '''
        Runs base2 primality test on n with k trials,
        returns 0 for composite, 1 for prime
    '''
    if pow(2,n-1,n)==1:
        return 1
    return 0

def miiller_test_helper(d, n):
     
    a = 2 + random.randint(1, n - 4);
 
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
    num1='0b1'
    for i in range(bitlength-2):
        num1 += choice(['0','1'])
    num1 += '1'
    num1=(int(num1,2))
    return num1


def generate_large_primes(bitlength):
    '''
        generates 2 large odd numbers of given bit length,
        runs fermat and M-R test and trial division for primality
        return 2 large primes of given bitlength

    '''
    num1=generate_large_odd(bitlength)
    num2=generate_large_odd(bitlength)
    
    while fermat_base2_test(num1) and miller_test(num1,4):
        num1=generate_large_odd(bitlength)
    while fermat_base2_test(num2) and miller_test(num2, 4):
        num2=generate_large_odd(bitlength)

    return num1,num2
    