from sortedcontainers import SortedList


class Num:
    def __init__(self, row: int, index: int, value):
        self.row   = row
        self.index = index
        self.value = value

class Solution632:
    def smallestRange(self, rows: list[list[int]]) -> list[int]:
        '''
        Повертає мінімальний діапазон, в якому є хоча б одне
        значення з кожного з відсортованих рядів `rows`.

        ```
        smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]) -> [20,24]
        #                       --             --        --

        ```
        '''

        nums: SortedList[Num] = SortedList(key=lambda num: num.value)

        min_range = [0,0]
        min_delta = float('inf')

        for i, row in enumerate(rows):
            nums.add(Num(i, 0, row[0]))
        
        while True:
            min_val = nums[0].value
            max_val = nums[-1].value
            delta = max_val - min_val
            
            if (delta < min_delta):
                min_range = [min_val, max_val]
                min_delta = delta
            
            for i in range(len(nums)):
                num = nums[i]

                if num.index + 1 < len(rows[num.row]):
                    nums.pop(i)
                    num.index += 1
                    num.value = rows[num.row][num.index]
                    nums.add(num)
                    break
            else:
                return min_range


s = Solution632()
print(s.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))