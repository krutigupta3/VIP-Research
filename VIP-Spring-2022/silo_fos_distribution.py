#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:03:43 2022

@author: guptahome
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


print('Data Visualization')

#read the output file

df = pd.read_csv('../../output_mod.csv', index_col=0)


#method to visualize the dataset


def visualize(param):
    print('Dataset before processing: \n', param)

    #prepare dataset (remove all inf and NaN values)
    param.replace([np.inf, -np.inf], np.nan)
    param.dropna()

    print('Dataset after processing: \n', df)
    
    #get the deformation mod values
    
    deformation_mod = (param.iloc[11,0:1000])
    
    print(deformation_mod)
    
    #display
    deformation_mod = deformation_mod[:-1]
    deformation_mod.hist(bins = 20)
    


#COHESION = 0 
# Causing the distribution to be skewed - almost normal without this

print('COHESION = 0')

df1 = df.iloc[:, 1::5]

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
