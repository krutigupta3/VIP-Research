#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 18:40:05 2022

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

from sklearn import metrics

from sklearn import svm
from sklearn import preprocessing



df = pd.read_csv('../output_mod.csv', index_col=0)

print('Dataset before processing: \n', df)

#prepare dataset (remove all inf and NaN values)
df.replace([np.inf, -np.inf], np.nan)
df.dropna()


#print(df[' 226'])
del df[' 111']
del df[' 226']
del df[' 231']
del df[' 246']
del df[' 351']
del df[' 361']
del df[' 476']
del df[' 481']
del df[' 496']
del df[' 726']
del df[' 731']
del df[' 976']
del df[' 981']



print('Dataset after processing: \n', df)


#create 2d array for input parameters 

list1 = (df.iloc[0, 0:987])
list2 = (df.iloc[1, 0:987])
list3 = (df.iloc[2, 0:987])
list4 = (df.iloc[3, 0:987])
list5 = (df.iloc[4, 0:987])
list6 = (df.iloc[5, 0:987])



x = np.transpose((list1, list2, list3, list4, list5, list6))


print('Input parameter array: \n', x)


print()

print('SVM MODEL RESULTS')


def create_svm_model(output):
    # split training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(x, output,test_size=0.2,random_state = 0)
    
    
    # label encoder
    le = preprocessing.LabelEncoder()
    y_train = le.fit_transform(y_train)
    y_test = le.fit_transform(y_test)
    
    ##Create a svm Classifier
    clf = svm.SVC(kernel='linear') # Linear Kernel

    #Train the model using the training sets
    clf.fit(X_train, y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    
    # Model Accuracy: how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


print('--- AREA REDUCED ---')
area_reduced = (df.iloc[6,0:995])
area_reduced = area_reduced[:-1]
create_svm_model(area_reduced)


print('--- PLASTIC ZONE ---')
plastic_zone = (df.iloc[7,0:995])
plastic_zone = plastic_zone[:-1]
create_svm_model(plastic_zone)



print('--- MAX PEEQ ---')
max_peeq = df.iloc[8,0:995]
max_peeq = max_peeq[:-1]
create_svm_model(max_peeq)


print('--- MIN PEEQ ---')
min_peeq = df.iloc[9,0:995]
min_peeq = min_peeq[:-1]
create_svm_model(min_peeq)

print('--- DEFORMATION MOD---')
deformation_mod = (df.iloc[10,0:995])
deformation_mod = (deformation_mod[:-1])
create_svm_model(deformation_mod)

print('--- FACTOR OF SAFETY ---')
silo_PoS = (df.iloc[11,0:995])
silo_PoS = silo_PoS[:-1]
create_svm_model(silo_PoS)







