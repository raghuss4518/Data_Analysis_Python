import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')

imputer = SimpleImputer(strategy='median')
imputer.fit(data[['Age']])
data[['Age']] = imputer.transform(data[['Age']])
print(data[['Age']])


#city value to fit
imputer = SimpleImputer(strategy = 'most_frequent')
imputer.fit(data[['City']])
data[['City']] = imputer.transform(data[['City']])
print(data[['City']])

#missing value
After_fill_Data = data.isnull().sum()
print(After_fill_Data)