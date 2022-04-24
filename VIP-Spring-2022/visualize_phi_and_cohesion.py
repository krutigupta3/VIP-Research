#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:34:47 2022

@author: guptahome
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


#import csv file wiht normalized data
print('Data Visualization using combination of 2 input variables')

df = pd.read_csv('../../output_mod.csv', index_col=0)

'''


def visualize(param):
    print('Dataset before processing: \n', param)

    #prepare dataset (remove all inf and NaN values)
    param.replace([np.inf, -np.inf], np.nan)
    param.dropna()

    print('Dataset after processing: \n', df)
    
    
    area_mod = (param.iloc[10,0:1000])
    
    print(area_mod)
    
    area_mod = area_mod[:-1]
    area_mod.hist(bins = 20)
'''

# remove unecessary data from data frame
df.replace([np.inf, -np.inf], np.nan)
df.dropna()
phi = df.iloc[3,0:1000]
cohesion = df.iloc[5,0:1000]
area_Reduced = (df.iloc[7,0:1000])
deformation_mod = (df.iloc[10,0:1000])
silo_fos = (df.iloc[11,0:1000])

def deformation(value1 , value2):
    array = []
    for i in range(len(phi)):
        
        if(phi[i] == value1 and cohesion[i] == value2):
            print(phi[i], cohesion[i], silo_fos[i])
            array.append(silo_fos[i])
            
    return array

def area(value1 , value2):
    array = []
    for i in range(len(phi)):
        
        if(phi[i] == value1 and cohesion[i] == value2):
            #print(phi[i], cohesion[i], area[i])
            array.append(area_Reduced[i])
            
    return array


print('deformation 1-----------------')
a1 = deformation(0,0) #outliers


print('deformation 2 -----------------')
a2 = deformation(0,0.25)

print('deformation 3 -----------------')
a3 = deformation(0,0.5)

print('deformation 4-----------------')
a4 = deformation(0,0.75)


print('deformation 5-----------------')
a5 = deformation(0,1)

print('deformation 6-----------------')
a6 = deformation(0.25,0) #outliers


print('deformation 7 -----------------')
a7 = deformation(0.25,0.25)

print('deformation 8-----------------')
a8 = deformation(0.25,0.5)

print('deformation 9-----------------')
a9 = deformation(0.25,0.75)


print('deformation 10-----------------')
a10 = deformation(0.25,1)

print('deformation 11-----------------')
a11 = deformation(0.5,0) #outliers


print('deformation 12 -----------------')
a12 = deformation(.5,0.25)

print('deformation 13 -----------------')
a13 = deformation(0.5,0.5)

print('deformation 14-----------------')
a14 = deformation(0.5,0.75)


print('deformation 15-----------------')
a15 = deformation(0.5,1)

print('deformation 16-----------------')
a16 = deformation(0.75,0) #outliers


print('deformation 17 -----------------')
a17 = deformation(0.75,0.25)

print('deformation 18-----------------')
a18 = deformation(0.75,0.5)

print('deformation 19-----------------')
a19 = deformation(0.75,0.75)


print('deformation 20-----------------')
a20 = deformation(0.75,1)



'''

b1 = area(0,0) #outliers


print('area 2 -----------------')
b2 = area(0,0.25)

print('area 3 -----------------')
b3 = area(0,0.5)

print('area 4-----------------')
b4 = area(0,0.75)


print('area 5-----------------')
b5 = area(0,1)

print('area 6-----------------')
b6 = area(0.25,0) #outliers


print('area 7 -----------------')
b7 = area(0.25,0.25)

print('area 8-----------------')
b8 = area(0.25,0.5)

print('area 9-----------------')
b9 = area(0.25,0.75)


print('area 10-----------------')
b10 = area(0.25,1)

print('area 11-----------------')
b11 = area(0.5,0) #outliers


print('area 12 -----------------')
b12 = area(.5,0.25)

print('area 13 -----------------')
b13 = area(0.5,0.5)

print('area 14-----------------')
b14 = area(0.5,0.75)


print('area 15-----------------')
b15 = area(0.5,1)

print('area 16-----------------')
b16 = area(0.75,0) #outliers


print('area 17 -----------------')
b17 = area(0.75,0.25)

print('area 18-----------------')
b18 = area(0.75,0.5)

print('area 19-----------------')
b19 = area(0.75,0.75)


print('area 20-----------------')
b20 = area(0.75,1)
#colors = ['orange','yellow','green','blue','turquoise', 'maroon', 'black', 'grey','light green']
'''
com = [a2, a3, a4, a5,a7,a8,a9,a10,a12,a13,a14,a15,a17,a18,a19,a20]
       #, b2, b3, b4, b5,b7,b8,b9,b10,b12,b13,b14,b15,b17,b18,b19,b20]
#com = [b2, b3, b4, b5,b7,b8,b9,b10,b12,b13,b14,b15,b17,b18,b19,b20]

plt.hist(com, bins=5)

'''
a3 = []
area(a3,0,0.5)
a4 = []
area(a4,0,0.75)
a5 = []
area(a5,0,1)
'''
'''
#COHESION = 0 
# Causing the distribution to be skewed - almost normal without this

print('COHESION = 0')

df1 = df.iloc[:, 1::5]
print(df1)

visualize(df1)

print('COHESION = .25')

df2 = df.iloc[:, 2::5]

visualize(df2)

print('COHESION = .5')

df3 = df.iloc[:, 3::5]

visualize(df3)

print('COHESION = .75')

df4 = df.iloc[:, 4::5]

visualize(df4)



'''