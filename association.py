# Importing libraries

# For importing, cleaning and transforming data
import numpy as np
import pandas as pd
import re
# For data analysis
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
# For visualisation
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the groceries df 
groceries_df=pd.read_csv(r'C:/Users/Win 10/Desktop/Market-Basket-Analysis/groceries_df.csv')
groceries_df

# Function to strip leading characters- Batch names O,Q and Y and empty spaces

import re

def rename_10(item_name):
    return re.sub(r'^[RS10]\s*', 'PEN', item_name)

groceries_df['Item Name'] = groceries_df['Item Name'].apply(rename_10)

def clean_item_name(item_name):
    return re.sub(r'^[OQXY]\s*', '', item_name)

# Apply function to 'Item Name' column
groceries_df['Item Name'] = groceries_df['Item Name'].apply(clean_item_name)

def removenum(item_name):
    return re.sub(r'^[\d.-]+\s*', '', item_name)

# Apply function to 'Item Name' column
groceries_df['Item Name'] = groceries_df['Item Name'].apply(removenum)

groceries_df

# Group by 'Bill Number' and create new columns for each item
df_grouped = groceries_df.groupby('Bill No')['Item Name'].apply(lambda x: pd.Series(x.values)).unstack().reset_index()
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

# importing the basket dataframe
basket_df=pd.read_csv(r'C:/Users/Win 10/Desktop/Market-Basket-Analysis/basket_df.csv')

# Filling the NaN values with the word 'NA'
basket_df.fillna('NA', inplace=True)

# Formatting dataframe into list of lists
basket_df_list = basket_df.values.tolist()

# Removing 'NA' from each list
for i in range(len(basket_df_list)):
    basket_df_list[i] = [x for x in basket_df_list[i] if not x=='NA']

# Transactional encoding
te = TransactionEncoder()
te_ary = te.fit(basket_df_list).transform(basket_df_list)

df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# Apriori Algorithm

frequent_itemsets = apriori(df_encoded, min_support=0.003, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.05)

# confidence tells us the how likely the consequent will be bought when the antecedents is bought
rules.sort_values(by='confidence', ascending=False).head(10)

# lift tells us the strength of the rule
rules.sort_values(by='lift', ascending=False).head(20)

frequent_itemsets.sort_values(by='support',ascending=False)

rules.sort_values(by='lift', ascending=False).drop(columns=['antecedent support','consequent support','leverage','conviction'])

#Customizable function to change the lift and confidence
def rules_mod(lift,confidence):
    '''rules_mod is a function to control the rules 
    based on lift and confidence threshold'''
    return rules[ (rules['lift'] >= lift) &
      (rules['confidence'] >= confidence) ]

#Calling function
rules_mod(lift=0.7,confidence=0.2)


# Visualise the results
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#Setting up the style
plt.figure(figsize = (15, 15))
sns.set_style('darkgrid')
#Plotting the relationship between the metrics
plt.subplot(2,2,1)
sns.scatterplot(x="support", y="confidence",data=rules)
plt.subplot(2,2,2)
sns.scatterplot(x="support", y="lift",data=rules)
plt.subplot(2,2,3)
sns.scatterplot(x="confidence", y="lift",data=rules)
plt.subplot(2,2,4)
sns.scatterplot(x="antecedent support", y="consequent support",data=rules)
plt.show()

pip install networkx
import networkx as nx
import re

sns.set_style("whitegrid")
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection = '3d')


x = rules['support']
y = rules['confidence']
z = rules['lift']

ax.set_xlabel("Support")
ax.set_ylabel("Confidence")
ax.set_zlabel("Lift")

ax.scatter(x, y, z)
ax.set_title("3D Distribution of Association Rules")

plt.show()

def draw_network(rules, rules_to_show):
  # Directional Graph from NetworkX
  network = nx.DiGraph()
  
  # Loop through number of rules to show
  for i in range(rules_to_show):
    
    # Add a Rule Node
    network.add_nodes_from(["R"+str(i)])
    for antecedents in rules.iloc[i]['antecedents']: 
        # Add antecedent node and link to rule
        network.add_nodes_from([antecedents])
        network.add_edge(antecedents, "R"+str(i),  weight = 2)
      
    for consequents in rules.iloc[i]['consequents']:
        # Add consequent node and link to rule
        network.add_nodes_from([consequents])
        network.add_edge("R"+str(i), consequents,  weight = 2)

  color_map=[]  
  
  # For every node, if it's a rule, colour as Black, otherwise Orange
  for node in network:
       if re.compile("^[R]\d+$").fullmatch(node) != None:
            color_map.append('black')
       else:
            color_map.append('orange')
  
  # Position nodes using spring layout
  pos = nx.spring_layout(network, k=16, scale=1)
  # Draw the network graph
  nx.draw(network, pos, node_color = color_map, font_size=8)            
  
  # Shift the text position upwards
  for p in pos:  
      pos[p][1] += 0.12

  nx.draw_networkx_labels(network, pos)
  plt.title("Network Graph for Association Rules")
  plt.show()

draw_network(rules, 10)

# Creating the bar plot
import plotly.express as px

fig = px.bar(rules, x=rules.index, y='support', text='support', labels={'index': 'Association Rule'})
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(title='Association Rules by Support', xaxis_title='Association Rule', yaxis_title='Support')
fig.show()

#Creating Scatter Plot
fig = px.scatter(rules, x='confidence', y='lift', title='Confidence vs Lift')
fig.update_traces(marker=dict(size=12, color='skyblue', line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))
fig.update_layout(xaxis_title='Confidence', yaxis_title='Lift', showlegend=False)
fig.show()

fig = px.scatter(rules, x='confidence', y='support', title='Confidence vs Support')
fig.update_traces(marker=dict(size=12, color='skyblue', line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))
fig.update_layout(xaxis_title='Confidence', yaxis_title='Lift', showlegend=False)
fig.show()

fig = px.scatter(rules, x='support', y='lift', title='Support vs Lift')
fig.update_traces(marker=dict(size=12, color='skyblue', line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))
fig.update_layout(xaxis_title='Confidence', yaxis_title='Lift', showlegend=False)
fig.show()

# Building a business application

milk_rules = rules[rules['consequents'].astype(str).str.contains('EGG')]
milk_rules = milk_rules.sort_values(by=['lift'],ascending = [False]).reset_index(drop = True)
display(milk_rules.head())
