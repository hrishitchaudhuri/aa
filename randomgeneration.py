"""Randomly generate DFT/FFT tests."""
import numpy as np
import matrix

from polynomial import Polynomial

def test_ffts(n):
    """
    Tests randomly generated vector of size n. 
    """
    arr = np.random.randint(0, 256, n)

    n1 = np.fft.fft(arr)

    arr = Polynomial(arr)
    d1 = arr.dft_regular()
    d2 = arr.dft_vandermonde()
    d3 = arr.fft_recursive()

    return (np.allclose(n1, d1, rtol=1e-3, atol=1e-3) 
            and np.allclose(d1, d2, rtol=1e-3, atol=1e-3)
            and np.allclose(d2, d3, rtol=1e-3, atol=1e-3))


def test_iffts(n):
    """
    Tests IFFT of a randomly generated vector of size n
    """
    arr = np.random.randint(0, 256, n)
    n_arr = np.fft.fft(arr)

    n1 = np.fft.ifft(n_arr)

    n_arr = Polynomial(dft=n_arr)
    a1 = n_arr.idft_vandermonde()
    a2 = n_arr.ifft_recursive()

    return (np.allclose(n1, a1, rtol=1e-3, atol=1e-3)
            and np.allclose(a1, a2, rtol=1e-3, atol=1e-3))


def test_grayscale(m, n):
    """
    Randomly generates m x n matrix and tests DFT-IDFT operation.
    """
    arr = np.random.randint(0, 256, m * n)
    arr.resize(m, n)

    m = matrix.matrix_compression(arr)

    return np.allclose(arr, m, rtol=1e-3, atol=1e-3)