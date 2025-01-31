import pandas as pd
import numpy as np

data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')
#print(data)

#filter_data = data(data['Age'].isna([49, 17]))
#print(filter)

data = [data['Income'].isin(['63333','78889'])]
print(data)