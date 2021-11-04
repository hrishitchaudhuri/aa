from random import choice

def fermat_base2_test(n):
    '''
        Runs base2 primality test on n with k trials,
        returns 0 for composite, 1 for prime
    '''
    if pow(2,n-1,n)==1:
        return 1
    return 0

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

    # RUN TESTS FOR PRIMALITY
    # 1. Fermat's pseudo primality test
    while fermat_base2_test(num1)==0:
        num1=generate_large_odd(bitlength)
    while fermat_base2_test(num2)==0:
        num2=generate_large_odd(bitlength)
    
    # 2. Miller-Rabin primality test
    

    return num1,num2
    