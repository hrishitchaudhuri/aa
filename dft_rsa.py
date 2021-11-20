'''Converting np arrays to/from bytes'''
from RSA import Keys, encrypt
from polynomial import Polynomial
import numpy as np
import rsa

def rsa_encryptarray(stream, pub):
    '''helper to encrypt arrays using rsa'''
    cipher = b''
    for i in range(len(stream) - 5):
        cipher += rsa.encrypt(stream[i: i + 4], pub)
        i = i + 5

    if cipher[i] != cipher[-1]:
        cipher += rsa.encrypt(stream[i:], pub)
    return cipher

def rsa_decryptarray(stream, priv, bsize):
    '''helper to decrypt arrays using rsa'''
    decipher = b''
    for i in range(len(stream) - bsize):
        decipher += rsa.decrypt(stream[i: i + bsize - 1], priv)
        i = i + bsize

    if decipher[i] != decipher[-1]:
        decipher += rsa.decrypt(stream[i:], priv)
    
    return decipher

def convert_arr_to_bytes(arr):
    '''numpy array to bytes'''
    return arr.tobytes()

def convert_bytes_to_arr(buffer, dtype=np.dtype('complex128')):
    '''bytes to numpy array'''
    return np.frombuffer(buffer, dtype=dtype)

if __name__ == '__main__':
    keys = Keys(128)

    e, d, N = keys.pub, keys.priv, keys.N
    a = Polynomial(np.random.randint(0, 256, 8))
    a_dft = a.dft_regular()
    a_dft_bytes = convert_arr_to_bytes(a_dft)

    cipher = encrypt(a_dft_bytes, e, N)
    decipher = encrypt(cipher, d, N)
    t = convert_bytes_to_arr(a_dft_bytes)
    d = convert_bytes_to_arr(decipher, dtype=a_dft.dtype)
    d = d[np.where(d != 0)]
    print(len(a_dft), len(d))
    print(t)
    print(d)
    print(np.allclose(a_dft, d, rtol=1e+001 or 1e+002 or 1e+003))
