import numpy as np
import pandas as pd

#loading April dataset
url1='https://raw.githubusercontent.com/dharanidaran-t/MarketBasketAnalysis/main/quick%20pick%20data%20month%20wise/april_df.csv'
df1=pd.read_csv(url1)
df1
df1.info()
#Checking for null values
df1.isna().sum()

#loading May dataset
url2=''

