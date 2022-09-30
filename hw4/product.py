"""
Write a class called Product. 
The class should have ﬁelds called name, amount, and price, holding the product’s name, the number of items of that product in stock, and the regular price of the product. 
There should be a method get_price that receives the number of items to be bought and returns a the cost of buying that many items, 
where the regular price is charged for orders of less than 10 items, 
a 10% discount is applied for orders of between 10 and 99 items, 
and a 20% discount is applied for orders of 100 or more items. 
There should also be a method called make_purchase that receives the number of items to be bought and decreases amount by that much.
"""

class Product:
    def __init__(self, name, amount=0, price=0):
        self.name= name
        self.__amount__ = amount
        self.__price__ = price

    def get_price(self, n):
        if self.__amount__ < n:
            return 0
        elif n>=0 and n<10:
            return self.__price__*n
        elif n>=10 and n<99:
            return self.__price__*0.9* n
        elif n>100:
            return self.__price__*0.8 * n

    def make_purchase(self, m):
        if self.__amount__ < m:
            return "Not enough"
        self.__amount__ -= m
        print(f"Product: {self.name} \n      Amount: {m}\n      Price: {self.get_price(m)}")
#        return self.get_price(m)

#    def __str__(self):
#        return f"Product: {self.name} \n      Amount: {self.__amount__}\n      Price: {self.__price__}"


stock = list()

apple = Product("apple", 100, 5)
stock.append(apple)
orange = Product("orange", 80, 10)
stock.append(orange)
grapes = Product("grapes", 50, 20)
stock.append(grapes)
milk = Product("milk", 60, 15)
stock.append(milk)
bread = Product("bread", 120, 8)
stock.append(bread)

n = int(input())
product_list = list()
total_price = 0

for i in range(n):
    to_buy = list(input().split())
    to_buy[1] = int(to_buy[1])
    product_list.append(to_buy)

for i in range(len(product_list)):
    for j in range(len(stock)):
        if product_list[i][0] == stock[j].name:
            stock[j].make_purchase(product_list[i][1])
            total_price += stock[j].get_price(product_list[i][1])

print(f"TOTAL: {total_price}")
