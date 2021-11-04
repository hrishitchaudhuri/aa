import numpy as np

from polynomial import Polynomial

def fft_2d(mtx):
    """
    Returns 2-D FFT of matrix
    """
    x, y = mtx.shape
    fft_matrix = []
    for i in range(x):
        print("ROW: ", i)
        temp = Polynomial(mtx[i])
        fft_matrix.append(temp.fft_recursive())

    fft_matrix = np.transpose(np.array(fft_matrix))

    fft_final = []
    x, y = fft_matrix.shape
    for i in range(x):
        print("COL: ", i)
        temp = Polynomial(fft_matrix[i])
        fft_final.append(temp.fft_recursive())

    fft_final = np.transpose(np.array(fft_final))
    return fft_final


def ifft_2d(dft2):
    """
    Returns 2-D matrix given a 2-D DFT.
    """
    x, y = dft2.shape
    orig_matrix = []
    for i in range(x):
        temp = Polynomial(dft=dft2[i])
        orig_matrix.append(temp.ifft_recursive())

    orig_matrix = np.transpose(np.array(orig_matrix))

    final_matrix = []
    x, y = orig_matrix.shape
    for i in range(x):
        temp = Polynomial(dft=orig_matrix[i])
        final_matrix.append(temp.ifft_recursive())

    final_matrix = np.transpose(np.array(final_matrix))
    return final_matrix


def matrix_compression(mtx):
    x, y = mtx.shape

    m1 = fft_2d(mtx)
    m2 = ifft_2d(m1)

    return m2[0:x, 0:y]