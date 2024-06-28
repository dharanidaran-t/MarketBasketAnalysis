#Importing Libraries
import pandas as pd

# For visualisation
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

#1-wordcloud
from wordcloud import WordCloud

#Importing Dataset
groceries_df
# RENAME COLUMN
groceries_df = groceries_df.rename(columns={'Item Name': 'title'})
#Checking the Data
groceries_df.head()
#Creating the text variable
text2 = " ".join(title for title in groceries_df.title)
# Creating word_cloud with text as argument in .generate() method
word_cloud2 = WordCloud(collocations = False, background_color = 'white').generate(text2)
# Display the generated Word Cloud
plt.imshow(word_cloud2, interpolation='bilinear')
plt.axis("off")
plt.show()

##2

# RENAME COLUMN
groceries_df = groceries_df.rename(columns={'title': 'Item Name'})

item_freq = groceries_df['Item Name'].value_counts().sort_values(ascending = False).head(25)

plt.figure(figsize=(10, 6))
item_freq.plot(kind='bar', color='wheat')
plt.xlabel('Item Name')
plt.ylabel('Frequency (absolute)')
plt.title('Top-25 Absolute Item Frequency Plot')
plt.show()

# 3- top 10 item frequecies
item_freq = groceries_df['Item Name'].value_counts().sort_values(ascending = False).head(10)
plt.figure(figsize=(8, 6))
item_freq.plot(kind='bar', color='blue')
plt.xlabel('Item Name')
plt.ylabel('Frequency (absolute)')
plt.title('Top-10 Absolute Item Frequency Plot')
plt.show()

# 4 Lets find the least 15 purchased item type
item_freq = groceries_df['Item Name'].value_counts().sort_values(ascending = False).tail(10).plot(kind='bar', color='seagreen', edgecolor='black')

plt.xlabel('Item types')
plt.ylabel('Purchase count')
plt.title('Least 15 purchased item types')

# 5 #bLets see if there is any different in the number of transactions month-wise

groceries_df['Month'].value_counts()
groceries_df['Month'].value_counts().sort_values(ascending = False).plot(kind='bar',edgecolor='black',color='green')
plt.title('Number of transactions month-wise')

# 6 transaction per weekday
plt.figure(figsize = (8,6))
groceries_df.groupby(groceries_df['Day of week'])['Bill No'].nunique().sort_values(ascending = False).plot(kind='bar',color='lightblue')
plt.xlabel('Week day')
plt.ylabel('Transactions')
plt.title('Transactions by Weekday')
plt.xticks(rotation=0)
plt.show()

# 7
# Highest sales amount items (Top 50)

import jinja2

cm = sns.light_palette('pink', as_cmap = True)
item_sales = groceries_df.groupby('Item Name')['Rate'].sum().sort_values(ascending= False)
item_sales.to_csv('ItemSales.csv')
item_sales = pd.read_csv('ItemSales.csv')
item_sales.head(50).style.background_gradient(cmap=cm)

# 8

# Least sales amount items (Least 20)
import jinja2

cm = sns.light_palette('pink', as_cmap = True)
item_sales = groceries_df.groupby('Item Name')['Rate'].sum().sort_values(ascending= False)
item_sales.to_csv('ItemSales.csv')
item_sales = pd.read_csv('ItemSales.csv')
item_sales.tail(20).style.background_gradient(cmap=cm)
