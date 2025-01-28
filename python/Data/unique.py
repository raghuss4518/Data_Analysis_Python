import pandas as pd
import numpy as np
from  sklearn.impute import SimpleImputer

data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')

print(data)

#print only first 5 line a value
#print(data.head())

# Print last five a value
#print(data.tail())

# Find out unique in value in Purchase_Channel
unique_value = data['Purchase_Channel'].unique()
print(unique_value)

#Find out a unique a value 
unique_value_CI = data['CustomerID'].unique()
print(unique_value_CI)

#Find out a unique a value in Gender a value
unique_value_G = data['Gender'].unique()
print(unique_value_G)

#Find out a unique value in Age cloumn
unAge = data['Age'].unique()
print(unAge)

#Find out a unique value in Income cloumn
U_N_In = data['Income'].unique()
print(U_N_In)

#Find out a unique value in Customer life  cloumn
U_N_C_L_M = data['Customer_Lifespan_Months'].unique()
print(U_N_C_L_M)

#Find out a unique value in Date cloumn
Un_Date = data['Date_of_Purchase'].unique()
print(Un_Date)

#Find out a unique value in Churn status cloumn
UN_CS = data['Churn_Status'].unique()
print(UN_CS)