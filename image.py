import cv2
import numpy as np

import matrix

# REFACTOR THIS ENTIRE FILE

atj = cv2.imread('images/atj_grayscale.jpg', 0)
# cv2.imwrite('images/atj_grayscale.png', atj)

# atj = cv2.imread('images/atj_grayscale.png', 0)
print(atj.shape)
x, y = atj.shape

n1 = np.fft.fft2(atj)

m1 = matrix.fft_2d(atj)

n2 = np.sort(np.abs(n1.reshape(-1)))
for keep in [0.1, 0.05, 0.01]:
    thresh = n2[int(np.floor((1 - keep) * len(n2)))]
    index = np.abs(n1) > thresh

    low = n1 * index

    n3 = np.fft.ifft2(low).real

    filename = 'images/atj_fft_' + str(keep * 100) + '.jpg'

    cv2.imwrite(filename, n3)


m2 = np.sort(np.abs(m1.reshape(-1)))
for keep in [0.1, 0.05, 0.01]:
    thresh = m2[int(np.floor((1 - keep) * len(m2)))]
    index = np.abs(m1) > thresh

    low = m1 * index

    m3 = matrix.ifft_2d(low).real

    filename = 'images/atj_hfft_' + str(keep * 100) + '.jpg'

    cv2.imwrite(filename, m3[0:x, 0:y])