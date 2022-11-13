#Count number of books of high price, middle, price and low price

import pandas as pd

data = pd.read_csv("Book_dataset_1.csv")

temp = data.Price.value_counts()

mid = data.describe()["Price"]["mean"]                                    #high-----mid_high-----mid-----mid_low-----low
high_mid = (mid + data.describe()["Price"]["max"] )/2                     #|    high   |        middle       |    low   |
low_mid = mid/2

cnt_high = 0
cnt_mid = 0
cnt_low = 0

for i in temp.keys():
    if i > high_mid:
        cnt_high += 1
    elif i < low_mid:
        cnt_low +=1
    else:
        cnt_mid +=1  

print(f"High --- {cnt_high}")
print(f"Middle --- {cnt_mid}")
print(f"Low --- {cnt_low}")
    
