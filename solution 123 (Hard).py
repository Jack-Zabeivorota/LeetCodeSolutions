class PriceData:
    def __init__(self, price: int , day: int = 0):
        self.price = price
        self.day = day
    
    def set(self, day: int, price: int):
        self.day = day
        self.price = price
    
    def set_from(self, data: 'PriceData'):
        self.price = data.price
        self.day = data.day


class Solution123:
    def get_min_max_price_and_first_delta(self, prices: list[int]) -> tuple[PriceData, PriceData, int]:
        max_price, min_price = PriceData(prices[0]), PriceData(prices[0])
        global_max_price, global_min_price = PriceData(prices[0]), PriceData(prices[0])
        first_delta = global_delta = 0

        for i, price in enumerate(prices):
            if price < min_price.price:
                min_price.set(i, price)
                max_price.set(i, price)

            elif price > max_price.price:
                max_price.set(i, price)

                delta = max_price.price - min_price.price

                if delta > global_delta:
                    global_max_price.set_from(max_price)

                    if min_price.day > global_min_price.day:
                        global_min_price.set_from(min_price)
                        first_delta = global_delta
                    
                    global_delta = delta
        
        return global_min_price, global_max_price, first_delta

    def get_correction(self, start: int, end: int, prices: list[int]) -> int:
        max_price = min_price = prices[start]
        corr = 0

        for i in range(start, end):
            price = prices[i]

            if price > max_price:
                max_price = min_price = price

            elif price < min_price:
                min_price = price
                corr = max(corr, max_price - min_price)
        
        return corr

    def get_last_delta(self, start: int, prices: list[int]) -> int:
        min_price = max_price = prices[start]
        delta = 0

        for i in range(start, len(prices)):
            price = prices[i]

            if price < min_price:
                min_price = max_price = price

            elif price > max_price:
                max_price = price
                delta = max(delta, max_price - min_price)
        
        return max(delta, max_price - min_price)

    def maxProfit(self, prices: list[int]) -> int:
        '''
        Повертає максимальний прибуток, який можно було заробити на різниці цін графіка `prices`,
        відкриваючи при цьому максимум дві угоди (одна покупка, один продаж), які йдуть підряд.

        ```
        '      5                 '
        '     / \              4 '
        ' 3--3   \        3   /  '
        '         \      / \ /   '
        '          \    /   1    '
        '           0--0         '
        '                        '
        maxProfit([3,3,5,0,0,3,1,4]) -> 6 (buy1: 3, sell1: 5, buy2: 0, sell2: 4)
        ```
        '''

        if not prices: return 0

        min_price, max_price, first_delta = self.get_min_max_price_and_first_delta(prices)
        correction = self.get_correction(min_price.day, max_price.day, prices)
        last_delta = self.get_last_delta(max_price.day, prices)

        return max_price.price - min_price.price + max(first_delta, correction, last_delta)


s = Solution123()
print(s.maxProfit([3,3,5,0,0,3]))     # -> 5
print(s.maxProfit([6,1,3,2,4,7,3]))   # -> 7
print(s.maxProfit([1,5,2,6,0,1]))     # -> 8