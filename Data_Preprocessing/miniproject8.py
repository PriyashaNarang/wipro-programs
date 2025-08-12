#MINI PROJECT
""" Q1 Use-Case: House Price Prediction
Dataset: melb_data.csv
The dataset can be downloaded melb_data.csv | Kaggle
Perform the following tasks:
Load the data in dataframe (Pandas)
Handle inappropriate data
Handle the missing data
Handle the categorical data
"""
import pandas as pd
df=pd.read_csv('melb_data.csv')
df.drop_duplicates(inplace=True)
df.Lattitude.fillna(round(df.Lattitude.mean()),inplace=True)
df.Longtitude.fillna(round(df.Longtitude.mean()),inplace=True)
df.Bedroom2.fillna(df.Bedroom2.median(),inplace=True)
df.Bathroom.fillna(df.Bathroom.median(),inplace=True)
df.Car.fillna(df.Car.median(),inplace=True)
df.Landsize.fillna(df.Landsize.median(),inplace=True)
df.BuildingArea.fillna(df.BuildingArea.median(),inplace=True)
df.YearBuilt.fillna(df.YearBuilt.median(),inplace=True)
df.CouncilArea.fillna(df.CouncilArea.mode()[0],inplace=True)
dataset1=pd.get_dummies(df.Type)
updated_dataset1=pd.concat([dataset1,df.iloc[:,[1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]]],axis=1)
print(updated_dataset1)