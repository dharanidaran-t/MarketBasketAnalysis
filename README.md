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

### **5.1 Associate Rule Mining with Apriori Algorithm**

### **What is Apriori?**

#### Apriori algorithm uses frequent itemsets to get association rules, but on the assumptions that:

1. All subsets of frequent itemsets must be frequent

2. Similarly incase of infrequent subset their parent set is infrequent too The algorithm works in such a way that a minimum support value is set and iterations happen with frequent itemsets. Itemsets and subsets are ignored if their support is below the threshold till there can’t be any removal.

##### *Association rule is related to the statement of “what’ with what”. This matter can be in a form of statement on transaction activity carried out by the customers at a supermarket. From that statement, there has a strong relation to the study of customer transaction data database to determine the habit of a purchased product with what product, thus, association rule is frequently referred as market basket analysis. The significance of an associative rule can be figured in the presence of two parameters, namely **support** and **confidence**. Support (supporting value) is the percentage of combinations of product items in the database. While confidence (certainty value) is a value to determine the strength of inter-item relationships in association rules.*

## We can utilize three core measures that are used in Association Rule Learning, which are: Support, Confidence, and Lift.

### **i. Support:**

 *It signifies the popularity of the item, if an item is less frequently bought then it will be ignored in the association.*


### **ii. Confidence:**

 It tells the likelihood of purchasing Y when X is bought.Sounds more like a conditional probability. Infact it is ! But it fails to check the popularity(frequency) of Y to overcome that we got lift.

### **iii. Lift:**

 It combines both confidence and support.A lift greater than 1 suggests that the presence of the antecedent increases the chances that the consequent will occur in a given transaction. Lift below 1 indicates that purchasing the antecedent reduces the chances of purchasing the consequent in the same transaction.





