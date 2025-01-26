import pandas as pd
import numpy as np

#Read A Data
data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')
#print(data)

# Missing values
missing_data = data.isnull().sum()
print(missing_data)

#To idntify all missing values
missing_data1 = data.isnull()
print(missing_data1)