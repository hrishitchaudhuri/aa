import math
import cmath
import numpy as np

class Polynomial:
    """
    A class to describe polynomials. 
    """

    def __init__(self, coef):
        """
        Polynomial constructor.
        """
        self.coef = np.array(coef)
        self.db = len(coef)


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
                v.append(root ** i)
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
                v.append((root ** -i) / self.db)
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

    def idft_vandermond(self):
        """
        Return and set coefficient vector using the inverse Vandermonde matrix.
        """
        self.generate_complex_roots()
        self.generate_inv_vandermonde(self.roots)

        self.coef = self.ivand @ self.dft

        return self.coef


#TODO: Set better tests
p = Polynomial([1, 3, 2, 4, 5])
print(p.dft_regular())
print(p.dft_vandermonde())
print(p.idft_vandermond())