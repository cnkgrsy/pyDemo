import pandas as pd
import numpy as np

# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Cenk\Desktop\odevler\Alistirmalar\data.csv', encoding= 'unicode_escape')

df.info()
df_str = df['Description'].map(str)
df[df_str.str.contains("?", regex=False)]

df[df['Description'].notna().str.contains("CREAM")]
#
# df['Purch_Day']= pd.to_datetime(df['InvoiceDate']).day_of_week
# df['Purch_Month']= pd.to_datetime(df['InvoiceDate']).dt.month
# df['Purch_Year']= pd.to_datetime(df['InvoiceDate']).dt.year

df['CustomerID'].value_counts()

df.groupby('CustomerID')['Country'].value_counts()
df['PurchaseTotal']= df['Quantity'] * df['UnitPrice']