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

print("Augmented matrix\n")
print(augmented_matrix)
for i in range(0,len(augmented_matrix)-1):  
    print("\nStage {0}\n".format(i+1))
    print(augmented_matrix)
    for j in range(1+i,len(augmented_matrix)):
         temp = augmented_matrix[j][i]
         mult = temp / augmented_matrix[i][i]
         augmented_matrix[j] = augmented_matrix[j] - (mult*augmented_matrix[i])         
print(augmented_matrix)

xn = augmented_matrix[len(augmented_matrix)-1][len(augmented_matrix)]/augmented_matrix[len(augmented_matrix)-1][len(augmented_matrix)-1]

for i in range(len(augmented_matrix)-1,-1,-1):
    count = 0
    for p in range(i+1,len(augmented_matrix)):
        count = count + augmented_matrix[i][p] * augmented_matrix[p] 
        
x = augmented_matrix[:,4:] 
count = 0        

for i in range(len(augmented_matrix)-1,-1,-1):
    for j in range(i+1,len(augmented_matrix)):
        x[i] = x[i] - augmented_matrix[i][j] * x[j]
    x[i] = x[i]/augmented_matrix[i][i]
    
print("\n-----Solution-----")
for i in range(0,len(x)):
    print("x{0} = {1}".format(i+1,x[i]))
           