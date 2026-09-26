class Solution:
    def buyChoco(self, prices, money):
        min1 = float('inf')
        min2 = float('inf')

        for price in prices:
            if price < min1:
                min2 = min1
                min1 = price
            elif price < min2:
                min2 = price

        cost = min1 + min2

        if cost <= money:
            return money - cost
        else:
            return money
        