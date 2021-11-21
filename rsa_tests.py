"""Testing for RSA Enc/Dec on Polynomials in PV form (Point Value)"""
import numpy as np
from random import random
from RSA import encrypt, Keys
from polynomial import Polynomial

def get_pv(pol: Polynomial) -> list:
    '''evaluate pv form of C(x) for polynomial pol'''
    return np.array( [ (x, pol.eval(x)) for x in [random() for _ in range(pol.degree)] ] )

def unit(arr, e, d, N) -> bool:
    '''unit test case for one pv form: arr'''
    c = encrypt(arr.tobytes(), e, N)
    if arr.tobytes() == encrypt(c, d, N):
        return True
    return False

def success_rate():
    '''testing for varying key sizes'''
    try:
        bitlens = [128, 256, 512, 1024, 2048]
        a = Polynomial(np.random.randint(0, 256, 128))
        for blen in bitlens:
            keys = Keys(blen)
            e, d, N = keys.pub, keys.priv, keys.N
            passed = 0
            for iter in range(100):
                pv = get_pv(a)
                if unit(pv, e, d, N): passed += 1
            print(f'passed {passed}% for {blen} bit key')
    except OverflowError or ValueError:
        print(f'error at iteration {iter} for {blen}')

if __name__ == '__main__':
    success_rate()