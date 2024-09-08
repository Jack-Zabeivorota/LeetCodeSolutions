from typing import TypeVar, Generic
from bisect import insort
from math import sqrt

T = TypeVar('T')


class SortedList(Generic[T]):
    def __init__(self):
        self._len = 0
        self._blocks: list[list[T]] = []
        self._min_size = 10
        self._max_size = self._min_size
    
    def _find_block(self, value: T) -> int:
        l, r = 0, len(self._blocks)

        while l < r:
            mid = (l + r) // 2

            if self._blocks[mid][-1] < value:
                l = mid + 1
            else:
                r = mid
            
        return l

    def add(self, value: T):
        if not self._blocks:
            self._blocks.append([value])
            self._len = 1
            return

        block_index = self._find_block(value)

        if block_index < len(self._blocks):
            block = self._blocks[block_index]
            insort(block, value)
        else:
            block = self._blocks[-1]
            block.append(value)
            block_index = len(self._blocks) - 1
        
        self._len += 1
        self._max_size = max(self._min_size, int(sqrt(self._len)))

        if len(block) > self._max_size:
            mid = len(block) // 2
            self._blocks[block_index] = block[:mid]
            self._blocks.insert(block_index + 1, block[mid:])

    def __getitem__(self, index: int) -> T:
        if index < 0 or index >= self._len:
            raise IndexError('sortedlist index out of range')
        
        for block in self._blocks:
            if index < len(block):
                return block[index]
            index -= len(block)

    def get_len(self) -> int:
        return self._len


class Solution295:
    '''Повертає медіану з відсортованного массиву'''

    def __init__(self):
        self.list: SortedList[int] = SortedList()
    
    def addNum(self, num: int):
        self.list.add(num)

    def findMedian(self) -> float:
        mid = self.list.get_len() // 2

        if self.list.get_len() % 2 == 0:
            return (self.list[mid-1] + self.list[mid]) / 2

        return self.list[mid]


s = Solution295()
s.addNum(1)
s.addNum(4)
s.addNum(10)
s.addNum(3)
s.addNum(8)
# 1 3 4 8 10
#     -
print(s.findMedian()) # -> 4

s = Solution295()
s.addNum(6)
s.addNum(10)
s.addNum(2)
s.addNum(6)
s.addNum(5)
s.addNum(0)
s.addNum(6)
s.addNum(4)
# 0 2 4 5 6 6 6 10
#       ---
print(s.findMedian()) # -> 5.5