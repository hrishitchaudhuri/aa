import numpy as np

import matrix

arr = np.random.randint(0, 256, 100 * 100)
arr.resize(100, 100)

m = matrix.matrix_compression(arr)

print(np.allclose(arr, m, rtol=1e-3, atol=1e-3))
