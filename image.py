import cv2
import numpy as np

import matrix

def numpy_compress_image(read_filename, write_filename, compression=0.1):
    img = cv2.imread(read_filename, 0)
    x, y = img.shape

    fourier_matrix = np.fft.fft2(img)

    fourier_matrix_sorted = np.sort(np.abs(fourier_matrix.reshape(-1)))
    threshold = fourier_matrix_sorted[int(np.floor((1 - compression) * len(fourier_matrix_sorted)))]

    indices = np.abs(fourier_matrix) > threshold
    low_values = fourier_matrix * indices

    final_matrix = np.fft.ifft2(low_values).real

    cv2.imwrite(write_filename, final_matrix)


def painpy_compress_image(read_filename, write_filename, compression=0.1):
    img = cv2.imread(read_filename, 0)
    x, y = img.shape

    fourier_matrix = matrix.fft_2d(img)

    fourier_matrix_sorted = np.sort(np.abs(fourier_matrix.reshape(-1)))
    threshold = fourier_matrix_sorted[int(np.floor((1 - compression) * len(fourier_matrix_sorted)))]

    indices = np.abs(fourier_matrix) > threshold
    low_values = fourier_matrix * indices

    final_matrix = matrix.ifft_2d(low_values).real

    cv2.imwrite(write_filename, final_matrix[0:x, 0:y])
