import cv2
import numpy as np

import matrix

# REFACTOR THIS ENTIRE FILE

atj = cv2.imread('atj_grayscale.jpg', 0)

print(atj.shape)

m1 = np.fft.fft2(atj)
m1 = np.fft.ifft2(m1)

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