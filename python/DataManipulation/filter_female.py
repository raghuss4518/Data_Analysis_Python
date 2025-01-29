import pandas as pd
import numpy as np

data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')
#print(data)

#Filter only female data
filter_Female_data = data[data['Gender']!= "Male"]
print(filter_Female_data)

#filter female Data
Income = data[data['Income'] >60000]
print(Income)