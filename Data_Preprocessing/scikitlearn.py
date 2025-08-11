#EXERCISES
"""Q1 Perform Data Preprocessing on melb_data.csv dataset with statistical perspective. The dataset 
can be downloaded from https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
df=pd.read_csv('melb_data.csv')
features=df.iloc[:,:-1]
num_cols_with_nan = ['Bedroom2', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'YearBuilt']
imputer = SimpleImputer(strategy='median',missing_values=np.nan)
features.loc[:,num_cols_with_nan] = imputer.fit_transform(features[num_cols_with_nan])
cat_cols = ['Suburb', 'Method']
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
bin_matrix = encoder.fit_transform(features[cat_cols])
features_selected_num = features[num_cols_with_nan].values
final_array = np.concatenate((bin_matrix, features_selected_num), axis=1)
print(final_array[:5])