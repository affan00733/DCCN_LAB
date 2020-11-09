# Group NO 6
# Raj Gorhekar 2018130013
# Afan Ansari 2019230064
# EXP 5 Task 2

import numpy as np

arr = [
    [1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 1],
]
n = 7
k = 4
G = np.array(arr)
m = np.array([1, 0, 1, 0])


def syndrome_decode(codeword, n, k, G):
    HT = np.transpose(
        np.concatenate((np.transpose(G[:, k:]), np.identity(n - k)), axis=1))
    S = np.array(np.mod(np.dot(codeword, HT), 2)),
    # print("H transpose : \n", HT, "\nSyndrome is : ", S[0])
    for row, i in zip(HT, range(n)):
        if np.array_equal(S[0], row):
            codeword[i] ^= 1
            return (codeword, ' Hence Error is Detected and Corrected', i)
    return (codeword, ' Hence No correction is necessary', -1)
