"""
Write a class called Investment with ﬁelds called principal and interest. The constructor should set the values of those ﬁelds. 
There should be a method called value_after that returns the value of the investment after n years. 
The formula for this is p(1+i)n, where p is theprincipal, and i istheinterestrate. 
It should also use thespecial method __str__ so that printing the object will result in something like below:

Principal - $1000.00, Interest rate - 5.12%
"""

class Investment:
    def __init__(self, stavka, summa):
        self.stavka = stavka
        self.summa = summa

    def value_after(self, n):
        return self.summa * (1 + self.stavka) * n

    def __str__(self):
        return f"Stavka if {self.stavka} \nSumma is {self.summa}"

deposit = Investment(10, 1000)
print(deposit.value_after(12))
print(deposit)
