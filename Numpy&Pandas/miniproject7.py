#MINI PROJECT
""" Q1. Use Case:
Perform the Outlier detection for the given dataset i.e. datasetExample

Dataset : datasetExample.csv

Perform the following task

Load the data in the DataFrame.

Detection of Outliers"""

import pandas as pd
import numpy as np
df=pd.read_csv('datasetExample.csv')
arr=df["EstimatedSalary"].values
Q1,Q3=np.percentile(arr,[25,75])
IQR=Q3-Q1
lr=Q1-(1.5*IQR)
ur=Q3+(1.5*IQR)
outliers_iqr=df[(df['EstimatedSalary']<lr)|(df['EstimatedSalary']>ur)]
print("Outliers detected:")
print(outliers_iqr)