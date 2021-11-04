import cv2
import numpy as np

import matrix

# REFACTOR THIS ENTIRE FILE

atj = cv2.imread('images/atj_grayscale.jpg', 0)

print(atj.shape)
x, y = atj.shape

m1 = np.fft.fft2(atj)

m2 = []
threshold = 500
for i in range(x):
    m2.append([])
    for j in range(y):
        if abs(round(m1[i][j].real)) < threshold:
            m2[i].append(0)
        else:
            m2[i].append(m1[i][j])

m1 = np.fft.ifft2(m2)

m2 = np.real(m1)

filename = 'images/atj_fft_' + str(threshold) + '.jpg'

cv2.imwrite(filename, m2)