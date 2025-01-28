import pandas as pd
import numpy as np

data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')

#filler_only_male_data
filler_only_male_data = data[data['Gender'] == 'Male']
print(filler_only_male_data)


#filler Imcome > 72504
data_72504_fillter  = data[data['Income'] > 72504]
print(data_72504_fillter)

#Filter data Purchase data as fillter 