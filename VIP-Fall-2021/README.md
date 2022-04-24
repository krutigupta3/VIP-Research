# VIP-Fall-2021
Compilation of code scripts from the Fall 2021 semester of Intelligent Tunneling subteam.

## Table of Contents
1. Overview
2. Data Normalization
3. Regression and Feature Selection

## Overview
As a part of the Intelligent Tunneling team of the Computation Modeling and Visulization in Geomechanics Research Group, I created a script to normalize the input and output parameters of collected data, created a linear regression model using the processed dataset, and performed some inital feature selection analysis. 

This project is created with:
* Java 
* Python


## Data Normalization
Goals of this task: 
Machine learning models learn a mapping from input variables to an output variable. However, because these variables measure different quantities, they may use different units and scales. This in turn may increase the diffcult of the problem being modeled and result in a large error gradient. 

By scaling the input and output variables when preparing regression data, we can eliminate these discrepancies. We rescaled the variables to a range between 0 and 1 using the equation y = (x - min)/(max-min).


Method:
1. The Normalize.java file reads the input_parameter.csv file into arrays for each parameter. 
2. Then, the minValue and maxValue functions are used to identify the min and max values in each array. 
3. Finally, we call the normalize() method for each parameter and write the results into the output.csv file. 

## Linear Regression and Feature Selection
Goals of Regression Task:
Linear regression model is a predictive model concerned with minimizing the error of a model/making the most accurate predictions. We use the hypothesis function for linear regression to make these predictions.
The cost function is used to measure how well a regression model is performing. The mean squared and root mean squared functions were used in this analysis. 

Method:

The regression.py is a heavily commented python script that performs the regression task using the scikit-learn libraries. 
1. First, we read the output.csv file and remove all inf and NaN data values
2. Next, we identify the desired input and output parameters for the model
	a. we create a 2d array, X, containing all input data values
	b. we create a 1d array, y, with the target values (different for each regression)
3. Then, import the method train_test_split from sklearn library which splits the data into training and testing sets. 80% of the data is taken as a training dataset.
4. Next, import linearRegression from scikit learn library adn fit the model over training dataset
5. Print the intercept, coefficients for each input parameter, adn coefficient of determination for each regression
6. Finally, create a predictive model using the target parameter testing set and calculate mse adn rmse values to evaluate model performance. 

Goals of Feature Selection Task:
We used feature selection to identify which features in the data contribute the most to the output parameter. This is important because having too many irrelevant gestures can decrease the accuracy of the model.

Method:

The regression.py utilizes the linear regression model defined in the section above, to fit a feature selection model.
1. Importthe RFE model from scikit learn. 
2. Fit the model over the input and output training sets
3. Print the ranking, which is calculated based on the coefficients of each input parameter 

## Next Steps
Going forward we can explore more predictive models and see if they are a better fit for the data. We can identify if they are better fit by analyzing the previously computed mse and rmse values. Further, we can eliminate less significant input parameters and perform regression with the new input set. 

