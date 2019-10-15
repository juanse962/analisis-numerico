import numpy as np

A = np.array([[1,2,4],
               [2,1,2],
               [4,2,3]])


def valores_y_vectores_con_np(A):
    
    valores, vectores = np.linalg.eig(A) 
    
    print("\nValores propios")
    print("{} {} ".format(valores,'\n') )
    print("Vectores propios")
    print("{} {} ".format(vectores,'\n') )
    
valores_y_vectores_con_np(A)