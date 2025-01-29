import pandas as pd
import numpy as np

data = pd.read_excel('D:/my-project/Data analysis/Data_Analysis/All-Serices/Python/Resources/Resources/customer_data.xlsx')
#print(data)

# Income greater then 60000 fillter data
Income = data[data['Income'] >60000]
print(Income)

#filter a methode as Query Methode
query_Methode = Income.query('Churn_Status == "Yes" ')
print(query_Methode)

#Query Methode with Age sorted
Age_filter = query_Methode.query('Age > 20')
print(Age_filter)


#Query Methode with the fillter Purchase Channel
Purachase_Methode = Age_filter.query('Purchase_Channel == "Online" ')
print(Purachase_Methode)