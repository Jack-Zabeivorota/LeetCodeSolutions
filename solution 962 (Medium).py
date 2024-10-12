from collections import deque


class Solution962:
    def maxWidthRamp(self, nums: list[int]) -> int:
        '''
        Повертає максимальну ширину між `i` i `j` (`j - i`) з массиву `nums`
        при умовах `i < j` та `nums[i] <= nums[j]`.

        ```
        maxWidthRamp([6,0,8,2,1,5]) -> 4
        #               i-------j

        ```
        '''

        stack = deque([0])
        
        for i in range(1, len(nums)):
            if nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        max_width, j = 0, len(nums) - 1

        while stack:
            if nums[stack[-1]] <= nums[j]:
                max_width = max(max_width, j - stack.pop())
            else:
                j -= 1
        
        return max_width


s = Solution962()
print(s.maxWidthRamp([9,8,1,9,4,0,4,1]))