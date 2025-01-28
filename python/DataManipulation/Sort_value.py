import pandas as pd
import numpy as np

# Read a file
data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')
#print(data)

#sort a value
sort_value = data.sort_values(by ='CustomerID', ascending=False)
print(sort_value)

sort_value1 = data.sort_values(by='CustomerID', ascending=True)
print(sort_value1)