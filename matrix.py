import numpy as np

from polynomial import Polynomial

class Matrix:
    def __init__(self, matrix):
        """
        Matrix constructor.
        """
        self.shape = matrix.shape
        self.matrix = matrix
        self.tmatrix = np.transpose(matrix)

    def fft_2d(self):
        """
        Returns 2-D FFT of matrix
        """
        x, y = self.shape
        fft_matrix = []
        for i in range(x):
            temp = Polynomial(self.matrix[i])
            fft_matrix.append(temp.fft_recursive())

        fft_matrix = np.transpose(np.array(fft_matrix))

        fft_final = []
        x, y = fft_matrix.shape
        for i in range(x):
            temp = Polynomial(fft_matrix[i])
            fft_final.append(temp.fft_recursive())

        fft_final = np.array(fft_final)
        return fft_final

