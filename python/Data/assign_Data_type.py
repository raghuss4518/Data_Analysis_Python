import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')
#print(data)

#identify a uniue a value
unvalue = data['Customer_Lifespan_Months'].unique()
print(unvalue)
print(unvalue.dtype)


# assign a correct data type
data = data[data['Customer_Lifespan_Months'] !='XXXX']

# Check the data type after cleaning
print(data['Customer_Lifespan_Months'].dtype)

# Assign a correct data type (convert to object if needed)
data['Customer_Lifespan_Months'] = data['Customer_Lifespan_Months'].astype('object')

print(data['Customer_Lifespan_Months'])