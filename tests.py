from polynomial import Polynomial 

#TODO: Set better tests
p = Polynomial([1, 3, 2, 4, 5, 0, 0, 0])
print(p.dft_regular())
print(p.dft_vandermonde())
print(p.fft_recursive())
print(p.idft_vandermond())

q = Polynomial([1, 2, 5, 8, 2])
print(p * q)

q.dft_vandermonde()

# print(p @ q)