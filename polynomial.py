"""Class to define polynomials."""
import math
import cmath
import numpy as np

def cround(complex_value):
    """
    Rounds complex numbers to four decimal places.
    """
    return round(complex_value.real, 4) + round(complex_value.imag, 4) * 1j

class Polynomial:
    """
    A class to describe polynomials.
    """

    def __init__(self, coef=None, dft=None):
        """
        Polynomial constructor.
        """
        if coef is not None and dft is not None:
            self.coef = np.array(coef)
            self.dft = np.array(dft) # establish test for checking
            self.degree = len(coef)

        elif coef is not None:
            self.coef = np.array(coef)
            self.degree = len(coef)
            self.dft = None

        elif dft is not None:
            self.dft = np.array(dft)
            self.degree = len(dft)
            self.coef = None

        else:
            raise ValueError('Please initialize either the coefficient or DFT vector')

        self.roots = None
        self.vand = None
        self.ivand = None


    def eval(self, pt_x):
        """
        Return polynomial evaluated at point pt_x.
        """
        eval_sum = 0
        for i in range(self.degree):
            eval_sum += self.coef[i] * (pt_x ** i)

        return eval_sum


    def generate_complex_roots(self):
        """
        Set complex root vector according to degree bound of Polynomial.
        """
        self.roots = []
        for i in range(self.degree):
            self.roots.append(cmath.exp(-2j * math.pi * i / self.degree))

        self.roots = np.array(self.roots)

        return self.roots

    def generate_vandermonde(self, roots):
        """
        Return and set Vandermonde matrix given a sequence of complex roots of unity.
        """
        self.vand = []
        for root in roots:
            values = []
            for i in range(self.degree):
                values.append(root ** i)
            self.vand.append(values)

        self.vand = np.array(self.vand)

        return self.vand


    def generate_inv_vandermonde(self, roots):
        """
        Return and set inverse Vandermonde matrix given a sequence of complex roots of unity.
        """
        self.ivand = []
        for root in roots:
            values = []
            for i in range(self.degree):
                values.append((root ** -i) / self.degree)
            self.ivand.append(values)

        self.ivand = np.array(self.ivand)

        return self.ivand


    def dft_regular(self):
        """
        Return and set DFT vector for Polynomial.
        """
        self.generate_complex_roots()

        self.dft = []
        for i in range(self.degree):
            self.dft.append(self.eval(self.roots[i]))

        self.dft = np.array(self.dft)

        return self.dft


    def dft_vandermonde(self):
        """
        Return and set DFT vector using the Vandermonde matrix.
        """
        self.generate_complex_roots()
        self.generate_vandermonde(self.roots)

        self.dft = self.vand @ self.coef

        return self.dft


    def idft_vandermonde(self):
        """
        Return and set coefficient vector using the inverse Vandermonde matrix.
        """
        self.generate_complex_roots()
        self.generate_inv_vandermonde(self.roots)

        self.coef = self.ivand @ self.dft

        return self.coef


    def fft_recursive(self):
        """
        Set and return DFT vector via Fast Fourier Transform.
        """
        if self.coef is None:
            raise ValueError('Please initialize coefficient vector.')

        log2degree = math.log10(self.degree) / math.log10(2)
        if math.floor(log2degree) != math.ceil(log2degree):
            self.coef = np.append(self.coef, np.zeros((2 ** math.ceil(log2degree)) - self.degree))
            self.degree = 2 ** math.ceil(log2degree)

        if self.degree == 1:
            self.dft = self.coef.copy()
            return self.dft

        omega_n = cmath.exp(-2j * math.pi / self.degree)
        omega = 1

        a_0 = []
        a_1 = []

        for i in range(self.degree):
            if i % 2:
                a_1.append(self.coef[i])
            else:
                a_0.append(self.coef[i])

        a_0 = Polynomial(a_0)
        a_1 = Polynomial(a_1)

        y_0 = a_0.fft_recursive()
        y_1 = a_1.fft_recursive()

        y_tot = np.zeros(self.degree, dtype=np.complex128)

        for k in range(int(self.degree / 2)):
            y_tot[k] = y_0[k] + omega * y_1[k]
            y_tot[k + int(self.degree / 2)] = y_0[k] - omega * y_1[k]
            omega *= omega_n

        self.dft = y_tot
        return self.dft


    def ifft_recursion(self):
        """
        Implements private recursion within inverse FFT.
        """
        if self.dft is None:
            raise ValueError('Please initialize DFT vector.')

        log2degree = math.log10(self.degree) / math.log10(2)
        if math.floor(log2degree) != math.ceil(log2degree):
            self.dft = np.append(self.dft, np.zeros((2 ** math.ceil(log2degree)) - self.degree))
            self.degree = 2 ** math.ceil(log2degree)

        if self.degree == 1:
            self.coef = self.dft.copy()
            return self.coef

        omega_n = cmath.exp(-2j * math.pi / self.degree)
        omega_n = 1 / omega_n
        omega = 1

        a_0 = []
        a_1 = []

        for i in range(self.degree):
            if i % 2:
                a_1.append(self.dft[i])
            else:
                a_0.append(self.dft[i])

        a_0 = Polynomial(dft=a_0)
        a_1 = Polynomial(dft=a_1)

        y_0 = a_0.ifft_recursion()
        y_1 = a_1.ifft_recursion()

        y_tot = np.zeros(self.degree, dtype=np.complex128)

        for k in range(int(self.degree / 2)):
            y_tot[k] = y_0[k] + omega * y_1[k]
            y_tot[k + int(self.degree / 2)] = y_0[k] - omega * y_1[k]
            omega *= omega_n

        self.coef = y_tot
        return self.coef


    def ifft_recursive(self):
        """
        Sets and returns coefficient vector using inverse FFT.
        """
        self.ifft_recursion()
        for i in range(self.degree):
            self.coef[i] /= self.degree

        return self.coef


    def __mul__(self, other):
        """
        Convolution loop on coefficient vectors.
        """
        m_0 = self.degree
        m_1 = other.degree

        length = m_0 + m_1 - 1

        w_arr = np.zeros(length)
        for i in range(m_0):
            for j in range(m_1):
                w_arr[i + j] += self.coef[i] * other.coef[j]

        return Polynomial(w_arr)


    def __matmul__(self, other):
        """
        Return Hadamard product of DFT vectors.
        """
        if (self.dft is None or other.dft is None):
            raise ValueError("Please initialize DFT vector.")

        return Polynomial(dft=np.multiply(self.dft, other.dft))
