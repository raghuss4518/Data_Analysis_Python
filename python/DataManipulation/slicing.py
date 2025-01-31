import pandas as pd
import numpy as np

data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')
#print(data)

#Slicing methode loc
#filter_Sliceing = data.loc[0:10, 'CustomerID':'Income']
#print(filter_Sliceing)


#slicing with loc
#data3 = data.iloc[0:20,1:6]
#print(data3)


# Filter multiple condiniton
#data4 = data [(data['City'] == 'Chicago') & (data['City'] == 'Houston')]
data4 = data[(data['City'] == 'Chicago') & (data['City'] == 'Houston')]

print(data4)