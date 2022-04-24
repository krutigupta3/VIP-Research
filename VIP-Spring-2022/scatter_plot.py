#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 18:02:15 2022

@author: guptahome


This python file is used to plot a scatter plot. The scatter plot displays the distribution of values
of a single output parameter with respect to a combination of two input parameters (cohesion and friction angle)

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


print('Scatter Plot')

df = pd.read_csv('../../output_mod.csv', index_col=0)

print('Dataset before processing: \n', df)

#prepare dataset (remove all inf and NaN values)
df.replace([np.inf, -np.inf], np.nan)
df.dropna()

#Input variables
phi = df.iloc[3,0:995]
cohesion = df.iloc[5,0:995]


#Output variables
area_reduced = (df.iloc[6,0:995])
plastic_zone = (df.iloc[7,0:995])
max_peeq = df.iloc[8,0:995]
min_peeq = df.iloc[9,0:995]
deformation_mod = (df.iloc[10,0:995])
silo_fos = (df.iloc[11,0:995])

'''
INPUT
    identifier: an int label that specifies a distinct pair of cohesion and friction values [1,20]
    value1: specific value of friction angle
    value2: specific value of cohesion
OUTPUT
    an array of values of the specified output parameter that result from the specified combination of inputs
'''
def scatter(identifier, value1, value2):
    array = []
    x = []
    for i in range(len(phi)):
        
        if(phi[i] == value1 and cohesion[i] == value2):
            print(phi[i], cohesion[i], deformation_mod[i])
            array.append(deformation_mod[i])
            x.append(identifier)
    
    plt.scatter(x,array)
            
    return array

'''

Here we call the scatter() function 20 times for each pair of cohesion and friction values.
The output parameter we are considering in this scenario is the deformation_modulus.

'''
print('deformation 1-----------------')
scatter(1,0,0)

print('deformation 2 -----------------')
scatter(2,0,0.25)

print('deformation 3 -----------------')
scatter(3,0,0.5)
print('deformation 4-----------------')
scatter(4,0,0.75)


print('deformation 5-----------------')
scatter(5,0,1)

print('deformation 6-----------------')
scatter(6,0.25,0)


print('deformation 7 -----------------')
scatter(7,0.25,.25)

print('deformation 8-----------------')
scatter(8,0.25,.5)

print('deformation 9-----------------')
scatter(9,0.25,0.75)


print('deformation 10-----------------')
scatter(10,0.25,1)

print('deformation 11-----------------')
a11 = scatter(11,0.5,0) #outliers


print('deformation 12 -----------------')
a12 = scatter(12,.5,0.25)

print('deformation 13 -----------------')
a13 = scatter(13,0.5,0.5)

print('deformation 14-----------------')
a14 = scatter(14,0.5,0.75)


print('deformation 15-----------------')
a15 = scatter(15,0.5,1)

print('deformation 16-----------------')
a16 = scatter(16,0.75,0) #outliers


print('deformation 17 -----------------')
a17 = scatter(17,0.75,0.25)

print('deformation 18-----------------')
a18 = scatter(18,0.75,0.5)

print('deformation 19-----------------')
a19 = scatter(19,0.75,0.75)


print('deformation 20-----------------')
a20 = scatter(20,0.75,1)
