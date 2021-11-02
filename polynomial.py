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
        self.coef = coef

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
        
        return self.roots

    def generate_vandermonde(self, roots):
        """
        Return and set Vandermonde matrix given a sequence.
        """
        self.vand = []
        for root in roots:
            v = []
            for i in range(self.db):
                v.append(root ** i)
            self.vand.append(v)

        return self.vand


    def dft_regular(self):
        """
        Return and set DFT vector for Polynomial.
        """
        self.generate_complex_roots()

        self.dft = []
        for i in range(self.db):
            self.dft.append(self.eval(self.roots[i]))

        return self.dft

    def dft_vandermonde(self):
        """
        Return and set DFT vector using the Vandermonde matrix.
        """
        self.generate_complex_roots()
        self.generate_vandermonde(self.roots)

        self.coef = np.array(self.coef)
        self.vand = np.array(self.vand)

        self.dft = self.coef @ self.vand

        return self.dft


#TODO: Set better tests
p = Polynomial([1, 3, 2, 4, 5])
print(p.dft_regular())
print(p.dft_vandermonde())