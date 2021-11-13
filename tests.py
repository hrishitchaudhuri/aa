"""Test cases for DFT, IDFT functions."""
from randomgeneration import *

pows = [2 ** i for i in range(2, 12)]

for n in pows:
    try:
        assert(test_ffts(n))
        print('Test case FFT on vector of size', n, 'PASSED')
    except:
        print('Test case FFT on vector of size', n, 'FAILED')

    try:
        assert(test_iffts(n))
        print('Test case IFFT on vector of size', n, 'PASSED')
    except:
        print('Test case IFFT on vector of size', n, 'FAILED')

    try:
        assert(test_grayscale(n, n))
        print('Test case 2D transforms on square matrix of size', n, 'PASSED')
    except:
        print('Test case 2D transforms on square matrix of size', n, 'FAILED')