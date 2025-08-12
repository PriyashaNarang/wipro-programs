#MINI PROJECT
"""Q1 Use Case: Diabetes Prediction
Perform Exploratory Data Analysis for the Diabetes Dataset.
Dataset: Diabetes.csv
The dataset can be downloaded from https://www.kaggle.com/datasets
Perform the following tasks
Load the data in the DataFrame
Data Pre-processing
Handle the Categorical Data
Perform Uni-variate Analysis
Perform Bi-variate Analysis"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
df=pd.read_csv('diabetes.csv')
print("Statistical Summary")
print(df.describe())
df.BMI.fillna(df.BMI.mean(),inplace=True)
df.DiabetesPedigreeFunction.fillna(df.DiabetesPedigreeFunction.mean(),inplace=True)
df.Pregnancies.fillna(df.Pregnancies.median(),inplace=True)
df.Glucose.fillna(df.Glucose.median(),inplace=True)
df.BloodPressure.fillna(df.BloodPressure.median(),inplace=True)
df.SkinThickness.fillna(df.SkinThickness.median(),inplace=True)
df.Insulin.fillna(df.Insulin.median(),inplace=True)
df.Outcome.fillna(df.Outcome.mode()[0],inplace=True)
datasetreq=pd.get_dummies(df.Outcome)
datasetreq.replace([True,False],[0,1],inplace=True)
wholedataset=pd.concat([df.iloc[:,0:8],datasetreq],axis=1)
print("Distribution plots")
sns.displot(df.BMI,kde=True)
plt.show()
sns.displot(df.DiabetesPedigreeFunction,kde=True)
plt.show()
sns.displot(df.Pregnancies,kde=True)
plt.show()
sns.displot(df.Glucose,kde=True)
plt.show()
sns.displot(df.BloodPressure,kde=True)
plt.show()
sns.displot(df.SkinThickness,kde=True)
plt.show()
sns.displot(df.Insulin,kde=True)
plt.show()
print("Joint Plot BMI VS Age")
sns.jointplot(x=df.Age,y=df.BMI,kind='reg')
plt.show()
print("Pairplot")
sns.pairplot(df,hue="Outcome")
plt.show()
print("HeatMap")
plt.figure(figsize=(10,10))
sns.heatmap(wholedataset.corr(),annot=True)
plt.show()
print("Box Plot BMI VS Age")
sns.boxplot(x=df.Age,y=df.BMI,data=df)
plt.show()
print("Pie Chart for Outcome")
df.Outcome.value_counts().plot(kind='pie')
plt.show()
print("Bar Chart for Outcome")
df.Outcome.value_counts().plot(kind='bar')
plt.show()
print("PairGrid Scatter")
var1=sns.PairGrid(df,hue="Outcome")
var1.map(plt.scatter).add_legend()
plt.show()
print("Scatter Plot")
sns.scatterplot(x="Age",y="BMI",hue="Outcome",data=df,)
plt.show()