#Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from wordcloud import WordCloud

#Importing Dataset
df = pd.read_csv("C:/Users/Win 10/Desktop/Market-Basket-Analysis/groceries_df.csv")

# Function to strip leading characters- Batch names O,Q and Y and empty spaces
import re

def clean_item_name(item_name):
    return re.sub(r'^[OQY]\s*', '', item_name)

# Apply function to 'Item Name' column
df['Item Name'] = df['Item Name'].apply(clean_item_name)
df

#Renaming column
df = df.rename(columns={'Item Name': 'items'})

#Checking the Data
df.head()

#Creating the text variable

text2 = " ".join(items for items in df.items)

# Creating word_cloud with text as argument in .generate() method

word_cloud2 = WordCloud(collocations = False, background_color = 'white').generate(text2)

# Display the generated Word Cloud

plt.imshow(word_cloud2, interpolation='bilinear')

plt.axis("off")

plt.show()
