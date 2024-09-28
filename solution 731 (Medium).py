class MyCalendarTwo:
    def __init__(self):
        self.books: list[tuple[int, int]] = []
    
    def _get_cross_period(self, period1: tuple[int, int], period2: tuple[int, int]) -> tuple[int, int] | None:
        start1, end1 = period1
        start2, end2 = period2

        if end1 <= start2 or end2 <= start1:
            return None

        if start2 <= start1 and end1 <= end2:
            return (start1, end1)
        elif start1 <= start2 and end2 <= end1:
            return (start2, end2)
        elif start1 < start2:
            return (start2, end1)
        else:
            return (start1, end2)

    def book(self, start: int, end: int) -> bool:
        '''
        Додає бронювання на період часу з `start` по `end`,
        якщо додавання не призведе до потрійного бронювання.

        Потрійне бронювання - це коли y 3-x періодах бронювання
        є спільний момент часу. 
        '''

        periods: list[tuple[int, int]] = []
        period = None

        for book in self.books:
            period = self._get_cross_period(book, (start, end))

            if period:
                for p in periods:
                    if self._get_cross_period(p, period):
                        return False

                periods.append(period)
        
        self.books.append((start, end))
        return True
        


c = MyCalendarTwo()
print(c.book(10, 20)) # -> True
print(c.book(50, 60)) # -> True
print(c.book(10, 40)) # -> True
print(c.book(5,  15)) # -> False
print(c.book(5,  10)) # -> True
print(c.book(25, 55)) # -> True

#   10----20
#   |   |  |       50----60
#   10--+-------40 |   |
#   |   |    |   | |   |
# 5----15    |   | |   |
# |  |       |   | |   |
# 5-10       |   | |   |
#            25-------55