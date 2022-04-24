#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:59:08 2021

@author: guptahome
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
import math
from sklearn.feature_selection import RFE



#import csv file wiht normalized data

df = pd.read_csv('output.csv', index_col=0)

print('Dataset before processing: \n', df)

#prepare dataset (remove all inf and NaN values)
df.replace([np.inf, -np.inf], np.nan)
df.dropna()


#print(df[' 226'])
del df[' 226']
del df[' 476']
del df[' 726']
del df[' 976']

print('Dataset after processing: \n', df)


#create 2d array for input parameters 

list1 = (df.iloc[0, 0:995])
list2 = (df.iloc[1, 0:995])
list3 = (df.iloc[2, 0:995])
list4 = (df.iloc[3, 0:995])
list5 = (df.iloc[4, 0:995])
list6 = (df.iloc[5, 0:995])


x = np.transpose((list1, list2, list3, list4, list5, list6))


print('Input parameter array: \n', x)



print ('-------------------------------\n')
#REGRESSION for output parameter 1
print('REGRESSION for output parameter 1')
#extract output results
area_reduced = (df.iloc[6,0:995])


#split the data into training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(x, area_reduced,test_size=0.2,random_state = 0)



#fit the model over the training dataset
model = LinearRegression()

reg = model.fit(X_train,y_train)

print('\n')

#print r^2 value and input var coefficients and intercept
print('R^2 ', reg.score(X_train, y_train))
print('INTERCEPT ',reg.intercept_)
print('COEFFICIENT ',reg.coef_)
print('\n')

#create predication model using test set
pred = model.predict(X_test)

#Calculate root mean squared error to evaluate model performance
mse = mean_squared_error(y_test,pred)
print('MSE : ', mse)
rmse = math.sqrt(mse)
print('RMSE : ', rmse , '\n')


print('Feature Selection Results \n')

#feature selection
rfe = RFE(model, 1)
ref = rfe.fit(X_train,y_train)
print('rfe support', rfe.support_)
print('rfe ranking ', rfe.ranking_)

print ('-------------------------------\n')
#REGRESSION for output parameter 2
print('REGRESSION for output parameter 2')
#extract output results
plastic_zone = (df.iloc[7,0:995])


#split the data into training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(x, plastic_zone, test_size=0.2,random_state = 0)



#fit the model over the training dataset
model = LinearRegression()

reg = model.fit(X_train,y_train)

print('\n')

#print r^2 value and input var coefficients and intercept
print('R^2 ', reg.score(X_train, y_train))
print('INTERCEPT ',reg.intercept_)
print('COEFFICIENT ',reg.coef_)
print('\n')

#create predication model using test set
pred = model.predict(X_test)

#Calculate root mean squared error to evaluate model performance
mse = mean_squared_error(y_test,pred)
print('MSE : ', mse)
rmse = math.sqrt(mse)
print('RMSE : ', rmse , '\n')


print('Feature Selection Results \n')

#feature selection
rfe = RFE(model, 1)
ref = rfe.fit(X_train,y_train)
print('rfe support', rfe.support_)
print('rfe ranking ', rfe.ranking_)
