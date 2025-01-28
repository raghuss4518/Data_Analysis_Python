import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data =  pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')

data = data.head()

print(data)

print(data.dtypes)