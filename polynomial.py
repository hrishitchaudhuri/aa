import math
import cmath
import numpy as np

def cround(cx):
    return round(cx.real, 4) + round(cx.imag, 4) * 1j

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
            self.db = len(coef)

        elif coef is not None:
            self.coef = np.array(coef)
            self.db = len(coef)
            self.dft = None

        elif dft is not None:
            self.dft = np.array(dft)
            self.db = len(dft)
            self.coef = None

        else:
            raise ValueError('Please initialize either the coefficient or DFT vector')

        self.vand = None
        self.ivand = None


    def eval(self, x):
        """
        Return polynomial evaluated at point x. 
        """
        sum = 0
        for i in range(self.db):
            sum += self.coef[i] * (x ** i)

        return sum


    def generate_complex_roots(self):
        """
        Set complex root vector according to degree bound of Polynomial.
        """
        self.roots = []
        for i in range(self.db):
            self.roots.append(cmath.exp(-2j * math.pi * i / self.db))
        
        self.roots = np.array(self.roots)

        return self.roots

    def generate_vandermonde(self, roots):
        """
        Return and set Vandermonde matrix given a sequence of complex roots of unity.
        """
        self.vand = []
        for root in roots:
            v = []
            for i in range(self.db):
                v.append(cround(root ** i))
            self.vand.append(v)

        self.vand = np.array(self.vand)

        return self.vand

    def generate_inv_vandermonde(self, roots):
        """
        Return and set inverse Vandermonde matrix given a sequence of complex roots of unity.
        """
        self.ivand = []
        for root in roots:
            v = []
            for i in range(self.db):
                v.append(cround((root ** -i) / self.db))
            self.ivand.append(v)

        self.ivand = np.array(self.ivand)

        return self.ivand


    def dft_regular(self):
        """
        Return and set DFT vector for Polynomial.
        """
        self.generate_complex_roots()

        self.dft = []
        for i in range(self.db):
            self.dft.append(cround(self.eval(self.roots[i])))

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

        for coef in self.coef:
            coef = cround(coef)

        return self.coef


    def fft_recursive(self):
        """
        Set and return DFT vector via Fast Fourier Transform.
        """
        if self.coef is None:
            raise ValueError('Please initialize coefficient vector.')

        log2db = math.log10(self.db) / math.log10(2)
        if (math.floor(log2db) != math.ceil(log2db)):
            self.coef = np.append(self.coef, np.zeros((2 ** math.ceil(log2db)) - self.db))
            self.db = 2 ** math.ceil(log2db)

        if self.db == 1:
            self.dft = self.coef.copy()
            return self.dft

        omega_n = cmath.exp(-2j * math.pi / self.db)
        omega = 1

        a_0 = []
        a_1 = []

        for i in range(self.db):
            if i % 2:
                a_1.append(self.coef[i])
            else:
                a_0.append(self.coef[i])

        a_0 = Polynomial(a_0)
        a_1 = Polynomial(a_1)

        y_0 = a_0.fft_recursive()
        y_1 = a_1.fft_recursive()

        y = np.zeros(self.db, dtype=np.complex128)

        for k in range(int(self.db / 2)):
            y[k] = cround(y_0[k] + omega * y_1[k])
            y[k + int(self.db / 2)] = cround(y_0[k] - omega * y_1[k])
            omega *= omega_n
        
        self.dft = y
        return self.dft


    def __ifft_recursion(self):
        """
        Implements private recursion within inverse FFT.
        """
        if self.dft is None:
            raise ValueError('Please initialize DFT vector.')

        log2db = math.log10(self.db) / math.log10(2)
        if (math.floor(log2db) != math.ceil(log2db)):
            self.dft = np.append(self.dft, np.zeros((2 ** math.ceil(log2db)) - self.db))
            self.db = 2 ** math.ceil(log2db)

        if self.db == 1:
            self.coef = self.dft.copy()
            return self.coef

        omega_n = cmath.exp(-2j * math.pi / self.db)
        omega_n = 1 / omega_n
        omega = 1

        a_0 = []
        a_1 = []

        for i in range(self.db):
            if i % 2:
                a_1.append(self.dft[i])
            else:
                a_0.append(self.dft[i])

        a_0 = Polynomial(dft=a_0)
        a_1 = Polynomial(dft=a_1)

        y_0 = a_0.__ifft_recursion()
        y_1 = a_1.__ifft_recursion()

        y = np.zeros(self.db, dtype=np.complex128)

        for k in range(int(self.db / 2)):
            y[k] = cround(y_0[k] + omega * y_1[k])
            y[k + int(self.db / 2)] = cround(y_0[k] - omega * y_1[k])
            omega *= omega_n
        
        self.coef = y
        return self.coef


    def ifft_recursive(self):
        """
        Sets and returns coefficient vector using inverse FFT. 
        """
        self.__ifft_recursion()
        for i in range(self.db):
            self.coef[i] /= self.db

        return self.coef


    def __mul__(self, other):
        """
        Convolution loop on coefficient vectors.
        """
        m = self.db
        n = other.db

        length = m + n - 1

        w = np.zeros(length)
        for i in range(m):
            for j in range(n):
                w[i + j] += self.coef[i] * other.coef[j] 

        return Polynomial(w)

    def __matmul__(self, other):
        """
        Return Hadamard product of DFT vectors.
        """
        if (self.dft is None or other.dft is None):
            raise ValueError("Please initialize DFT vector.")
        
        return Polynomial(dft=np.multiply(self.dft, other.dft))