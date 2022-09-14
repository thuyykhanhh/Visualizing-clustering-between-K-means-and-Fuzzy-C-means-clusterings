import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
import sys

try:
    data_path = sys.argv[1]
    new_name = sys.argv[2]
except:
    print("Cần cung cấp dữ liệu")

df = pd.read_csv(data_path)
#Making data frame from excelfile
#Check and remove any NULL data
df = df.dropna(axis = 0, how ='any') # Drop null values
filtered_data = df[~df['Product Name'].str.contains('Freeze')] #remove outdated data
#remove outliners
filtered_data = filtered_data[~filtered_data['Product Name'].str.contains('Membership_1D')]
filtered_data = filtered_data[~filtered_data['Full name'].str.contains('Test')]
filtered_data = filtered_data[~filtered_data['Full name'].str.contains('DayOne')]
filtered_data = filtered_data[~filtered_data['Full name'].str.contains('Speak')]
filtered_data = filtered_data[~filtered_data['Full name'].str.contains('Một Ngày 2021')]
filtered_data = filtered_data[~filtered_data['Full name'].str.contains('One Day2020')]
filtered_data = filtered_data[~filtered_data['Product Name'].str.contains('JoiningFee_2M')]

def process_membership(product_name):
    if 'Membership' in product_name or 'JoiningFee' in product_name:
        name, meta = product_name.split(' ')
        meta = meta.split('_')[0][1:] # remove (
        return f'{name}_{meta}'
    return product_name

filtered_data['Product Name'] = filtered_data['Product Name'].apply(process_membership)
filtered_data = filtered_data[~filtered_data['Product Name'].str.contains('JoiningFee_2M')]
filtered_data = filtered_data[~filtered_data['Product Name'].str.contains('Membership_1D')]

product_min_price = filtered_data[['Product Name', 'Regular price']].groupby('Product Name').agg(lambda x: x[x > 0].min())

for row in product_min_price.iterrows():
    filtered_data.loc[filtered_data['Product Name'] == row[0], 'Regular price'] = row[1].values[0]

filtered_data['Regular price'] = filtered_data['Regular price'] * filtered_data['Quantity']

filtered_data.to_csv(new_name, index=False)
