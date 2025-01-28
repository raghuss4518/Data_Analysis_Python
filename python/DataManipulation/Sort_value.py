import pandas as pd
import numpy as np

# Read a file
data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')
#print(data)

#sort a value ascending=False
sort_value = data.sort_values(by ='CustomerID', ascending=False)
print(sort_value)

#print sort a value ascending=True
sort_value1 = data.sort_values(by='CustomerID', ascending=True)
print(sort_value1)

#sort a value Gender ascending=True
sort_gender = data.sort_values(by='Gender', ascending=True)
print(sort_gender)

#print sort a value ascending=False
sort_value2 = data.sort_values(by='Gender', ascending=False)
print(sort_value2)