import numpy as np

def oneD(pathtodataset):
    with open(pathtodataset,'w') as cv:
        for power in range(2,12):
            cv.write(f'{list(np.random.random(2**power))}\n')
    cv.close()