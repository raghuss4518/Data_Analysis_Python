import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

#Select data from 
data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')
#print(data)

# identify a duplicate a value
duplicate = data.duplicated()
print(duplicate)

#Replace a value
assign_Value = data.drop_duplicates(inplace=True)

#After replce a value 
print(assign_Value)