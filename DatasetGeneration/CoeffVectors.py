import numpy as np

with open('./Datasets/coefficient_vectors.txt','w') as cv:
    for power in range(2,12):
        cv.write(f'{list(np.random.random(2**power))}\n')