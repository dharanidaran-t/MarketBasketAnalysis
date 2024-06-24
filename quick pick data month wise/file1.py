import numpy as np
import pandas as pd

# Loading April dataset
url1='https://raw.githubusercontent.com/dharanidaran-t/MarketBasketAnalysis/main/quick%20pick%20data%20month%20wise/april_df.csv'
df1=pd.read_csv(url1)
df1

# Loading May dataset
url2='https://raw.githubusercontent.com/dharanidaran-t/MarketBasketAnalysis/data-preprocessing/quick%20pick%20data%20month%20wise/may_df.csv'
df2=pd.read_csv(url2)
df2

# Loading June data
url3='https://raw.githubusercontent.com/dharanidaran-t/MarketBasketAnalysis/data-preprocessing/quick%20pick%20data%20month%20wise/june_df.csv'
df3=pd.read_csv(url3)
df3

#Loading July data
url4='https://raw.githubusercontent.com/dharanidaran-t/MarketBasketAnalysis/data-preprocessing/quick%20pick%20data%20month%20wise/july_df.csv'
df4=pd.read_csv(url4)
df4

# Loading August dataset
url5='https://raw.githubusercontent.com/dharanidaran-t/MarketBasketAnalysis/data-preprocessing/quick%20pick%20data%20month%20wise/august_df.csv'
df5=pd.read_csv(url5)
df5

# Loading September dataset
url6='https://raw.githubusercontent.com/dharanidaran-t/MarketBasketAnalysis/data-preprocessing/quick%20pick%20data%20month%20wise/september_df.csv'
df6=pd.read_csv(url6)
df6

#Loading October dataset
url7='https://raw.githubusercontent.com/dharanidaran-t/MarketBasketAnalysis/data-preprocessing/quick%20pick%20data%20month%20wise/october_df.csv'
df7=pd.read_csv(url7)
df7

# Summary of dataframes
df1.info()
df2.info()
df3.info()
df4.info()
df5.info()
df6.info()
df7.info()5

# Checking for null values
df1.isna().sum()
df2.isna().sum()
df3.isna().sum()
df4.isna().sum()
df5.isna().sum()
df6.isna().sum()
df7.isna().sum()

''' There is no missing values in the dataset 
Hence, let us merge all the datasets into a df'''

# Concatenating dataframes row-wise (stack)
combined_df = pd.concat([df1, df2, df3, df4, df5, df6, df7], ignore_index=True)
# Setting ignore_index=True ensures that the resulting dataframe has a continuous index.
combined_df

combined_df.info()
combined_df.isna().sum()

# Seperating date,month,day from the dataframe using pandas datetime format
combined_df['Date']=pd.to_datetime(combined_df['Date'])
combined_df.info()
combined_df['Year'] = combined_df['Date'].dt.year
combined_df['Month'] = combined_df['Date'].dt.month
combined_df['Day'] = combined_df['Date'].dt.day
combined_df['Day of week'] = combined_df['Date'].dt.day_name()
combined_df
combined_df.to_csv(r'C:/Users/Win 10/Desktop/Market-Basket-Analysis/groceries_df.csv',index=False)
combined_df['Bill No'].unique()
combined_df['Bill No'].nunique()

'''Combined sales df is now saved in a  new csv file (groceries_df)
Now, let us create a new df to analyzes patterns of co-occurrence.
In this dataframe, we will display the items purchased together by a Bill No in a Single row 
(i.e., Displaying the items purchased by a person in a single purchase column-wise).'''

# Group by 'Bill Number' and create new columns for each item
df_grouped = combined_df.groupby('Bill No')['Item Name'].apply(lambda x: pd.Series(x.values)).unstack().reset_index()
# Rename columns
df_grouped.columns = ['Bill Number'] + [f'{i+1}' for i in range(df_grouped.shape[1]-1)]
df_grouped=df_grouped.drop(columns=['Bill Number'])
df_grouped.head(20)

# Drop the rows which has NaN value at the 2nd column (column index 1)
df_grouped = df_grouped.dropna(subset=[df_grouped.columns[1]], axis=0)
# Drop columns from 11 to 77
df_grouped.drop(columns=df_grouped.columns[10:77], inplace=True)
df_grouped.head(20)
df_grouped

#Save to new csv file
df_grouped.to_csv(r'C:/Users/Win 10/Desktop/Market-Basket-Analysis/basket_df.csv',index=False)
