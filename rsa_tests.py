"""Testing for RSA Enc/Dec on Polynomials in PV form (Point Value)"""
import random
import numpy as np

import rsa
import keys
import polynomial

def get_pv(pol):
    """
    Evaluates PV form of C(x) for polynomial.
    """
    return np.array([(x, pol.eval(x)) for x in [random.random() for _ in range(pol.degree)]])

def unit(arr, enc, dec, num):
    """
    Unit test case for one PV form.
    """
    cipher = rsa.encrypt(str(arr).encode(), enc, num)
    if str(arr) == rsa.decrypt(cipher, dec, num).decode():
        return True
    return False

def success_rate():
    """
    Test cases for varying key sizes.
    """
    try:
        bitlens = [128, 256, 512, 1024, 2048]
        test = polynomial.Polynomial(np.random.randint(0, 256, 8))

        for blen in bitlens:
            key = keys.Keys(blen)
            public, private = key.pub, key.priv

            passed = 0
            for _ in range(100):
                test_pv = get_pv(test)
                if unit(test_pv, public[0], private[0], public[1]):
                    passed += 1

            print(f'passed {passed}% for {blen} bit key')
    except (OverflowError, ValueError):
        print(f'error at iteration {iter} for {blen}')

if __name__ == '__main__':
    success_rate()
