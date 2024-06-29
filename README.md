# Market Baket Analysis Approach to Machine Learning

## 1. Introduction
  * Market basket analysis is a data mining technique that analyzes patterns of co-occurrence and determines the strength of the link between products purchased together. We also refer to it as frequent itemset mining or association analysis.
  * Market Basket Analysis is an **Unsupervised machine learning** algorithm performed on customer behavior whilst shopping at a supermarket through the means identifying association and connections among various items placed by the customers in their shopping baskets. In specific, Market Basket Analysis aims at simultaneously identifying the most frequently-purchased items by customers. Here, item is depicted as several kinds of products in supermarket. Using market basket analysis mode, a knowledge of what are the items oftenly purchased by the customers simultaneously and having an opportunity to be promoted can be obtained. With regards to the objective of market basket analysis mode to decide which products that customers purchase at the same time, whereby the name of this mode is taken from the behavior of the customers in placing shopping products into their shopping baskets or shopping list. Over identifying shopping basket pattern of a customer will significantly be able to help a company in using that information in respect of business strategy needs, one of them is placing the most frequently-purchased products simultaneously into one specific area.
    
    ![image](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/58a29f48-52be-4b19-b4b1-e1f72a348066)


## 2. Data prerequisite:
  * For conducting market Baket Analysis approach to Machine Learning, I have collected secondary-data from a departmental store opposite to Pondicherry University (where majority of customers will be my college students and nearby local peoples in Kalapet).
  * In this study, market analysis application will be implemented at Quick-Pick Departmental Store (Near Pondicherry University Kalapet), in regard with its inability to use transaction data. This application is expected to work well and is able to generate the desired result.

## 3. Objective

The objective of this study is to achieve the following:

1. To take the information from the super market and apply machine learning to predict what we need to do in the future.
2. To apply data analysis in our thesis. Where we will have our research process of inspecting, cleansing, transforming and modeling data to discover useful information, informing conclusions, and supporting decision-making.
3. To apply data mining, We will be applying MBA approach to machine learning. There we will try to understand the customer's purchase behaviour.
   
   ![image-4](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/d8a53907-df5f-400f-acb7-377b2d581b9e)

## 4. Exploratory Data Analysis
![image-8](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/30ac79c9-8b8e-4c72-8947-f30645c7859e)

### Image Cloud of Itemsets:
![image](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/9947d6bf-5577-4347-9e46-67f3c510380a)

### Top 10 Items- Bar Plot:

![image](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/84856e21-5dd2-4774-9ff8-f04b8e7b4571)

### Month-wise analysis:

![image](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/fd1468f6-e560-4b79-814e-0f0a3bbb1e25)

### Weekday analysis:

![image](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/b9be87c8-550c-463e-aa56-34fe6872af8d)

## 5. Research Methodology:

![image-6](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/d63942ac-05eb-4df3-9957-2a39a0a75438)

### **5.1 Associate Rule Mining with Apriori Algorithm**

### **What is Apriori?**

#### Apriori algorithm uses frequent itemsets to get association rules, but on the assumptions that:

1. All subsets of frequent itemsets must be frequent

2. Similarly incase of infrequent subset their parent set is infrequent too The algorithm works in such a way that a minimum support value is set and iterations happen with frequent itemsets. Itemsets and subsets are ignored if their support is below the threshold till there can’t be any removal.
   
![image-7](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/f623e4f2-b083-42dc-8b82-777e0ed63b4a)

##### *Association rule is related to the statement of “what’ with what”. This matter can be in a form of statement on transaction activity carried out by the customers at a supermarket. From that statement, there has a strong relation to the study of customer transaction data database to determine the habit of a purchased product with what product, thus, association rule is frequently referred as market basket analysis. The significance of an associative rule can be figured in the presence of two parameters, namely **support** and **confidence**. Support (supporting value) is the percentage of combinations of product items in the database. While confidence (certainty value) is a value to determine the strength of inter-item relationships in association rules.*

## We can utilize three core measures that are used in Association Rule Learning, which are: Support, Confidence, and Lift.

### **i. Support:**

 *It signifies the popularity of the item, if an item is less frequently bought then it will be ignored in the association.*


### **ii. Confidence:**

 It tells the likelihood of purchasing Y when X is bought.Sounds more like a conditional probability. Infact it is ! But it fails to check the popularity(frequency) of Y to overcome that we got lift.

### **iii. Lift:**

 It combines both confidence and support.A lift greater than 1 suggests that the presence of the antecedent increases the chances that the consequent will occur in a given transaction. Lift below 1 indicates that purchasing the antecedent reduces the chances of purchasing the consequent in the same transaction.
 
 ![image-2](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/b4f52d0b-16f5-4440-851f-6abdba1ae72e)

### **5.2 Visualising the Association rules**

#### Creating a Bar Plot

![image](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/674c6ac7-41a2-43c3-9f12-3decc27e9014)

#### Creating Scatter plot

###### To visualize our association rules, we can plot them in a 3D scatter plot. Rules that are closer to top right are the rules that can be the most meaningful to be further dived in.

![image](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/e902a752-8ee3-4b26-9010-31a54df9f652)

#### Sub-Plots

![image](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/9cf5f90a-5e58-4dc6-bba0-88efce1b6327)

#### **Insights**

- Support-confidence and Lift-Confidence has a linear relationship, which means that the most frequent items have some other items associated to it.

- When it come to the relationship between Lift and Support, it is squashed when it goes beyond 0.10.

- In antecedent and consequent support relationship there is no linear relationship but it’s rather inverse ,when consequent support increases the antecedent support fades out, we can consider this phenomenon as when Bread quantity of purchase increases the quantity of Butter fades.

#### Creating a Network Graph

![image](https://github.com/dharanidaran-t/MarketBasketAnalysis/assets/173265740/516fc8d1-7aa0-4045-8712-d93583cf6ee6)

### **Insights**

##### It is simpler to visualize with the help of network diagram than seeing in a tabular format. The arrow coming to the rules(orange circle) is from antecedents and the arrows going from rules circle are towards consequents.

# **5.3 Business Application**

##### *Let’s say the grocery has bought up too much Egg and is now worrying that the stocks will expire if they cannot be sold out in time. To make matters worse, the profit margin of Whole Milk is so low that they cannot afford to have a promotional discount without killing too much of their profits. One approach that can be proposed is to find out which products drive the sales of Whole Milk and offer discounts on those products instead.*


# 6. Inferences & Conclusions:

#### (i) Exploratory Data Analysis (EDA)

- **Duration of the Dataset:** The dataset covers the daily sales report over a period of 7-month, from 2022-04-01 to 2022-10-31.

- **Number of Unique Itemsets:** The dataset contains 13,434 variety of unique Items. It includes Groceries, Vegetables, Stationaries, Snacks and other Miscellaneous categories.

- **Number of Purchases:** Over the 7-month period, the dataset recorded 84,625 unique Purchases, showcasing the buying patterns of the customers.

- **Weekly Sales Analysis:** Weekly sales data indicates a consistent pattern of purchasing during week days, but the sale is low during weekends. It shows the purchasing need of the students during week-day.

- **Monthly Sales Analysis:** Monthly sales data reveals trends such as increased purchases during the August month, July recorded the least sale comparing to any other months.

- **Most purchasing products:** From the Bar Plot, we infer that Egg, Cloth bag records the most number of sales count followed by Vegetable items, Snacks, Groceries and Stationaries (Preferably more Pens were bought by the customers). In the vegetable category, Onion, Potato, green chillies Carrot and Lemon, Potato  are the most bought items. Milk and Curd are the most bought itemsets from Groceries section. Also, from the word-cloud image we clearly note that Snack items such as Biscuits-particularly Britannia items, Chocolates, Chips, Soft-drinks, Cakes records the most sales.

- **Maximum sales in terms of Price:** We infer that Bed records the highest Amount of sales eventhough it is mostly bought during the admission. Followed by Green-chillies, Onion, Tomato records the highest amount of sales which suggests that there is high need of vegetables and grocery items.

#### (ii) Market Basket Analysis using Apriori Algorithm

The Apriori algorithm was applied to the dataset to identify frequent itemsets and association rules. The key findings include:

- **Onion-Tomato & Green Chilli-Tomato:** These combinations were found to be one of the most frequently purchased together, indicating that customers commonly buy these vegetables simultaneously.

- **Vegetables-Bread-Egg:** Along with the Vegetables combination, Egg-Bread pairs are also frequently bought together, suggesting a pattern in the customer's cooking habits.

- **Bed-Pillow:** This combination indicates a strong association between these bedding items, reflecting a common shopping behavior for home essentials.

The Apriori classification method efficiently identified these frequent itemsets by analyzing the transactions and determining the Support, Confidence and Lift levels of the item pairs.

#### (iii) Suggestions for the Departmental Store

1. **Promotional Bundling:** Create bundled promotions for frequently bought together items like Onion-Tomato-Green Chilli, Egg-Bread and Bed-Pillow. This can encourage customers to buy more and increase sales volume.
  
2. **Cross-Merchandising:** Place related items together in the store to make it easier for customers to find and purchase these items, enhancing their shopping experience. Since, Vegetables and Groceries are the most bought categories together placing these two categories closely can boost the sales. Similarly for Snacks and Stationaries.

3. **Inventory Management:** Ensure that frequently paired items are always in stock to avoid missed sales opportunities. Regularly monitor inventory levels for these items and adjust stock accordingly.

4. **Targeted Marketing:** Utilize the insights from the market basket analysis to design targeted marketing campaigns. For example, send personalized offers to customers who frequently buy onions and tomatoes together.

5. **Layout Optimization:** Organize the store layout to reflect the common buying patterns identified. For instance, placing vegetables that are often bought together in close proximity can streamline the shopping process for customers.

*By implementing these strategies, the departmental store can enhance customer satisfaction, boost sales, and improve overall operational efficiency.*

# **References**

1. Raich, B. Ganguly, and M. Tota, "Machine Learning for Market Basket Analysis through," IOSR Journal of Engineering (IOSRJEN), pp. 22-23, 2019. 
2. https://www.researchgate.net/publication/355894565_Market_Basket_Analysis_Approach_to_Machine_Learning
3. https://www.researchgate.net/publication/365489098_MARKET_BASKET_ANALYSIS_FOR_A_SUPERMARKET
4. https://www.kaggle.com/code/mukandkrishna/mba-apriori
