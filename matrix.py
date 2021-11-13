"""Implements 2-D FFT operations"""
import numpy as np

from polynomial import Polynomial

def fft_2d(mtx):
    """
    Returns 2-D FFT of matrix
    """
    rows = mtx.shape[0]
    fft_matrix = []
    for i in range(rows):
        temp = Polynomial(mtx[i])
        fft_matrix.append(temp.fft_recursive())

    fft_matrix = np.transpose(np.array(fft_matrix))

    fft_final = []
    rows = fft_matrix.shape[0]
    for i in range(rows):
        temp = Polynomial(fft_matrix[i])
        fft_final.append(temp.fft_recursive())

    fft_final = np.transpose(np.array(fft_final))
    return fft_final


def ifft_2d(dft2):
    """
    Returns 2-D matrix given a 2-D DFT.
    """
    rows = dft2.shape[0]
    orig_matrix = []
    for i in range(rows):
        temp = Polynomial(dft=dft2[i])
        orig_matrix.append(temp.ifft_recursive())

    orig_matrix = np.transpose(np.array(orig_matrix))

    final_matrix = []
    rows = orig_matrix.shape[0]
    for i in range(rows):
        temp = Polynomial(dft=orig_matrix[i])
        final_matrix.append(temp.ifft_recursive())

    final_matrix = np.transpose(np.array(final_matrix))
    return final_matrix


def matrix_compression(mtx):
    """
    Sends matrix through DFT-IDFT transforms to test compatibility with original matrix.
    """
    rows, cols = mtx.shape

    mat_1 = fft_2d(mtx)
    mat_2 = ifft_2d(mat_1)

    return mat_2[0:rows, 0:cols]
