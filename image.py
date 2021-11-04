import cv2
import numpy as np

import matrix

# REFACTOR THIS ENTIRE FILE

atj = cv2.imread('atj_grayscale.jpg', 0)

print(atj.shape)
x, y = atj.shape

m1 = np.fft.fft2(atj)
m1 = np.fft.ifft2(m1)

m2 = []
for i in range(x):
    m2.append([])
    for j in range(y):
        m2[i].append(round(m1[i][j].real))

m2 = np.array(m2)

cv2.imwrite('atj_fft_2.jpg', m2)
"""
with open('atj_fft.txt', 'w') as atj:
    for i in range(x):
        for j in range(y):
            atj.write(str(int(m2[i][j])) + " ")
        atj.write("\n")
"""
"""
m2 = matrix.matrix_compression(atj)

print(np.allclose(m1, m2, rtol=1e-3, atol=1e-3))

with open('np.txt', 'w') as n:
    x, y = m1.shape
    for i in range(x):
        for j in range(y):
            n.write(str(m1[i][j]))
        n.write("\n")

with open('hc.txt', 'w') as h:
    x, y = m2.shape
    for i in range(x):
        for j in range(y):
            h.write(str(m2[i][j]))
        h.write("\n")
"""