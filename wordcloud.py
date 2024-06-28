#Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from wordcloud import WordCloud

#Importing Dataset

df = pd.read_csv("C:/Users/Win 10/Desktop/Market-Basket-Analysis/groceries_df.csv")
#Renaming column
df = df.rename(columns={'Item Name': 'title'})
#Checking the Data

df.head()

#Creating the text variable

text2 = " ".join(title for title in df.title)

# Creating word_cloud with text as argument in .generate() method

word_cloud2 = WordCloud(collocations = False, background_color = 'white').generate(text2)

# Display the generated Word Cloud

plt.imshow(word_cloud2, interpolation='bilinear')

plt.axis("off")

plt.show()
