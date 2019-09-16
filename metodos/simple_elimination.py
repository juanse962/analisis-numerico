#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:13:31 2019

@author: juan
"""

import numpy as np

A = np.array([[2,-1,0,3],
              [1,0.5,3,8],
              [0,13,-2,11],
              [14,5,-2,13]])
B = np.array([1,1,1,1])

augmented_matrix = np.insert(A,len(A),B,axis=1)

num = 0
for i in range(0,len(augmented_matrix)-1):  
    if num == 0:
        print("Augmented matrix\n")
        print(augmented_matrix)
    else:
        print("\nStage {0}\n".format(num))
        print(augmented_matrix)
    num += 1
    for j in range(1+i,len(augmented_matrix)):
        temp = augmented_matrix[j][i]
        mult = temp / augmented_matrix[i][i]
        augmented_matrix[j] = augmented_matrix[j] - (mult*augmented_matrix[i])   
print("\nStage {0}\n".format(num))      
print(augmented_matrix)
        
x = list(augmented_matrix[:,4]) 
count = 0        
for i in range(len(augmented_matrix)-1,-1,-1):
    for j in range(i+1,len(augmented_matrix)):
        x[i] = x[i] - augmented_matrix[i][j] * x[j]
    x[i] = x[i]/augmented_matrix[i][i]
    
print("\n-----Solution-----")
for i in range(0,len(x)):
    print("x{0} = {1}".format(i+1,x[i]))