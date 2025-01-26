import pandas as pd
import numpy as np

data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')
data1 = data.head()
print(data1)


data2 = data.tail()
print(data2)

print(data)