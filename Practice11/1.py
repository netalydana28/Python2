#https://www.kaggle.com/datasets/jalota/books-dataset?resource=download   <-- Dataset Link

"""
Used pandas funtions
value_counts()    2.py, 3.py
sort_values()     3.py
DataFrame()       4.py
Series()          3.py
Describe()        2.py
"""

#Count number of books in each category; Write value_counts function

import pandas as pd

data = pd.read_csv("Book_dataset_1.csv")

category = data.Category
unique_categories = set(category)
dict_categories = {}

for i in range(len(category)):
    if category[i] not in dict_categories.keys():
        dict_categories[category[i]] = 1
    else: 
        dict_categories[category[i]] += 1

for i in dict_categories.keys():
    print(f"{i} --- {dict_categories[i]}")