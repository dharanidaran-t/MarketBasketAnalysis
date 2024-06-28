# For importing, cleaning and transforming data
import numpy as np
import pandas as pd

# For data analysis
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# For visualisation
import matplotlib.pyplot as plt
import pandas as pd

############################################## Code-1  ######################################
importing cleaned basket dataframe

basket_df=pd.read_csv(r'C:/Users/Win 10/Desktop/Market-Basket-Analysis/basketpractice.csv')
print(basket_df)
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

print(frequent_itemsets.head(10))
# confidence tells us the how likely the consequent will be bought when the antecedents is bought
print(rules.sort_values(by='confidence', ascending=False).head(10))

# lift tells us the strength of the rule
print(rules.sort_values(by='lift', ascending=False).head(20))

################################ code-2 ####################################
basket1=(groceries_df.groupby(['Bill No','Item Name'])['Qty']
        .sum().unstack().reset_index().fillna(0)
        .set_index('Bill No'))

def encode_unit(x):
    if x<= 0:
        return 0
    if x>0:
        return 1
basket1_sets=basket1.map(encode_unit)

freq_itemsets_apr=apriori(basket1_sets,min_support=0.01,use_colnames=True)
rules_apr=association_rules(freq_itemsets_apr, metric="lift", min_threshold=0.05)

#Freq Items
freq_itemsets_apr.sort_values(by='support',ascending=False)

##################################################################
# This code will rise Memory Error - It requires too much memory #
##################################################################

# To process the whole dataset, This requires storage around 8gb - too much storage so we are using groceries dataset
### Since it takes too much memory to process the whole basket, Lets analyse the baskets month-wise
groceries_df=pd.read_csv(r'C:/Users/Win 10/Desktop/Market-Basket-Analysis/groceries_df.csv')
groceries_df

basket1=(groceries_df[groceries_df['Month']=="April"]
        .groupby(['Bill No','Item Name'])['Qty']
        .sum().unstack().reset_index().fillna(0)
        .set_index('Bill No'))

def encode_unit(x):
    if x<= 0:
        return 0
    if x>0:
        return 1
basket1_sets=basket1.map(encode_unit)

freq_itemsets_apr=apriori(basket1_sets,min_support=0.01,use_colnames=True)
rules_apr=association_rules(freq_itemsets_apr, metric="lift", min_threshold=0.05)

#Freq Items
freq_itemsets_apr.sort_values(by='support',ascending=False)

# confidence tells us the how likely the consequent will be bought when the antecedents is bought
# lift tells us the strength of the rule
rule1=rules_apr.sort_values(by='lift', ascending=False).drop(columns=['antecedent support','consequent support','leverage','conviction','zhangs_metric'])
rule1
