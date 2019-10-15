import numpy as np


A = np.array([[5,0,4],
              [2,12,5],
              [2,3,6]]) #True
# A = np.array([[5,0,4],[4,12,8],[2,3,6]]) #False


def dd(A):
    D = np.diag(np.abs(A)) 
    S = np.sum(np.abs(A), axis=1) - D 
    if np.all(D > S):
        return True
    else:
        return False

print(dd(A))