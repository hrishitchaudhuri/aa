import numpy as np
from polynomial import Polynomial 
from matrix import Matrix

#TODO: Set better tests

p = Polynomial([1, 3, 2, 4, 5, 0, 0, 0])
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