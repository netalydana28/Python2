#Print out approximately 100 most available books

import pandas as pd

data = pd.read_csv("Book_dataset_1.csv")

temp = data.Avilability.value_counts().sort_values()

top_available = list()
cnt = 0

for i in temp.keys():
    cnt += temp[i]
    top_available.append(i)
    if cnt >= 100:
        break

x = list(data.Avilability)
books = pd.Series(data = x, index = data.Title)

for i in books.keys():
    if books[i] in top_available:
        print(i)