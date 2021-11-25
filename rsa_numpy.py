'''Converting np arrays to/from bytes'''
import numpy as np
import math
from random import randint, random, randrange
from RSA import Keys, encrypt, decrypt
from polynomial import Polynomial

def convert_arr_to_bytes(arr):
    '''numpy array to bytes, along with datatype'''
    return arr.tobytes(), arr.dtype

def convert_bytes_to_arr(buffer, dtype):
    '''bytes to numpy array'''
    d = np.frombuffer(buffer, dtype=dtype)
    return d

if __name__ == '__main__':
    keys = Keys(128)
    e, d, N = keys.pub, keys.priv, keys.N
    print(e, d, N)
    a = Polynomial(np.random.randint(0, 256, 128))
    pv = np.array(list((x, int(a.eval(x))) for x in [random() for _ in range(a.degree)]))

    print("ENCRYPT:")
    pvb = str(pv).encode('ascii')
    cipher = encrypt(pvb, e, N)
    
    print("DECRYPT:")
    decipher = decrypt(cipher, d, N).decode('ascii')
    # d = np.frombuffer(decipher, dtype=pv.dtype)
    print(pvb.decode())
    print(decipher)
    print(pvb.decode('ascii') == decipher)
    # print(len(d), d)
    # np.allclose(pv.flatten(), d[:128])
