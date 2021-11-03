import numpy as np
from polynomial import Polynomial 
import matrix

#TODO: Set better tests
"""
p = Polynomial([1, 3, 2, 4, 5])
print(p.dft_regular())
print(p.fft_recursive())
print(np.fft.fft(p.coef))

df = Polynomial(dft=p.dft)

print(np.fft.ifft(df.dft))
print(df.idft_vandermond())
print(df.ifft_recursive())
# q = Polynomial([1, 2, 5, 8, 2])
# print(p * q)

# q.dft_vandermonde()

# print(p @ q)

mat = np.array([[2, 4], [3, 5]])
mat = Matrix(mat)

print(mat.fft_2d())
print(np.fft.fft2(mat.matrix))
"""

a1 = [1, 5, 6, 2, 3]
a2 = [4, 2, 9, 3, 9]

p = Polynomial(a1)
q = Polynomial(a2)

c1 = p * q

m = len(a1)
n = len(a2)

for i in range(m - 1):
    a2.append(0)

for i in range(n - 1):
    a1.append(0)

p = Polynomial(a1)
q = Polynomial(a2)

p.fft_recursive()
q.fft_recursive()

c2 = p @ q

c2.ifft_recursive()

# print(c1.coef)
# print(c2.coef)


mat = np.array([[2, 5, 4, 3, 2], [9, 3, 1, 5, 1], [12, 14, 1, 13, 4], [25, 9, 1, 2, 5], [11, 14, 19, 2, 13]])
m1 = matrix.matrix_compression(mat)
m2 = np.fft.fft2(mat)
m2 = np.fft.ifft2(m2)
print(m1)
print(m2)

print(np.allclose(m1, m2, rtol=1e-3, atol=1e-5))