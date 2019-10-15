import numpy as np
import sympy 


A = np.array([[4,-1,1],
              [-1,4.25,2.75],
              [1,2.75,3.5]]) #True
# A = np.array([[9,7],[6,14]]) #False


def is_pos_def(A): 
    if np.array_equal(A, A.T): 
     try: 
      np.linalg.cholesky(A) 
      return True 
     except LinAlgError: 
      return False 
    else: 
     return False 

print(is_pos_def(A))