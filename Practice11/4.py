#Graphic Category -- Price

"""
to do:
1. count middle price for every category:
   1.1. value counts
   1.2 whole sum of prices 
2. plot the graph
"""

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Book_dataset_1.csv")

category = data.Category #Category column set
categories_quantity = category.value_counts() #Values count of every cetagory

graph_dictionary = {} #Will store category and middle price data
categories_price_sum = pd.DataFrame(data, columns = ['Category', 'Price']) #Creating data frame with Category and Price columns
for i in range(len(category)):
    rslt = categories_price_sum[categories_price_sum['Category'] == category[i]]
    graph_dictionary[category[i]] = int(sum(rslt["Price"])/categories_quantity[category[i]])#divide total sum price of quantity

plt.barh(list(graph_dictionary.keys()), graph_dictionary.values(), color = "green")
plt.title("Category - MiddlePrice Graph")
plt.xlabel("Price")
plt.ylabel("Category")
plt.show()