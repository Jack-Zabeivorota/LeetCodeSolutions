from typing import List

class Solution41:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        Повертає перше найменше пропущене позитивне число в листі `nums`.
        ```
        firstMissingPositive([-2,-5,8,1,2,0]) -> 3
        ```
        '''
        
        set_nums = set(num for num in nums if num > 0)

        min_num = 1
        while min_num in set_nums:
            min_num += 1
        return min_num

s = Solution41()
print(s.firstMissingPositive([1,2,0]))