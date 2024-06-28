# Importing libraries
# For importing, cleaning and analysing data
import numpy as np
import pandas as pd
groceries_df=pd.read_csv(r'C:/Users/Win 10/Desktop/Market-Basket-Analysis/groceries_df.csv')
groceries_df

# Function to strip leading characters- Batch names O,Q and Y and empty spaces
import re
def clean_item_name(item_name):
    return re.sub(r'^[OQXY]\s*', '', item_name)
# Apply function to 'Item Name' column
groceries_df['Item Name'] = groceries_df['Item Name'].apply(clean_item_name)
def removenum(item_name):
    return re.sub(r'^[\d.-]+\s*', '', item_name)
# Apply function to 'Item Name' column
groceries_df['Item Name'] = groceries_df['Item Name'].apply(removenum)
def rename_o(item_name):
    return re.sub('NION*', 'ONION', item_name)
groceries_df['Item Name'] = groceries_df['Item Name'].apply(rename_o)
def rename_10(item_name):
    return re.sub(r'^[RS10]\s*', 'PEN', item_name)

groceries_df['Item Name'] = groceries_df['Item Name'].apply(rename_10)
groceries_df
groceries_df.sample(20)
# Checking for NaN values
groceries_df.isna().sum()
# Dropping data with negative or zero quantity
negativeorNull = groceries_df.loc[groceries_df['Qty']<=0]
print('Count of Null or negative quantity: ', len(negativeorNull))
#Dropping data with zero or negative price
negativeorNull = groceries_df.loc[groceries_df['Rate']<=0]
print('Count of Null or negative Price: ', len(negativeorNull))
# Check 'Year' column for unique values
groceries_df['Year'].unique()
# Check 'Month' column for unique values
groceries_df['Month'].unique()
# Check 'Day' column for unusual values
groceries_df['Day'].unique()
# Check 'Day of week' column for unusual values
groceries_df['Day of week'].unique()
# Lets find out the time period of the dataset
print(f"The dataset is from dates {groceries_df['Date'].min()} to {groceries_df['Date'].max()}")
# Summary statistics
groceries=groceries_df.drop(columns=['Year','Day'],axis=1)
groceries.describe()
groceries_df.groupby(['Year', 'Month']).describe()
# Lets find how many unique purchases have been done
groceries_df['Bill No'].unique()
purchases=groceries_df['Bill No'].nunique()
print(f"There are {purchases} unique Purchases.")
Items=groceries_df['Item Name'].unique()
Items
# Lets find how many unique items are there in the dataset
n_items=groceries_df['Item Name'].nunique()
print(f"There are {n_items} unique Items")
CountOfItem = groceries_df['Item Name'].value_counts()
sortedItems = CountOfItem.sort_values(ascending=False)
df=pd.DataFrame(list(sortedItems.items()),columns=['Item name','Counts'])
df
print('Top 50 items:\n',df.head(50))
# Lets find the least 15 purchased item type
df.tail(15)
groceries_df.groupby(['Month'])['Amount'].sum()
print(groceries_df['Month'].value_counts())
groceries_df.groupby(['Day of week'])['Amount'].sum()
print(groceries_df['Day of week'].value_counts())
  
# Lets find out the top 20 Bill's where most number of items purchased
groceries_df['Bill No'].value_counts().head(10)

# Rate is the total price column
groceries_df.groupby(['Year', 'Month'])['Rate'].sum()
