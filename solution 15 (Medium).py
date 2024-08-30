class Solution15:
    def __three_exists(self, threes: list[list[int]], three: list[int]) -> bool:
        for t in threes:
            three_is_finded = True

            for num in three:
                if not num in t:
                    three_is_finded = False
                    break

            if three_is_finded: return True
                
        return False

    def __three_zero_exists(self, nums: list[int]) -> bool:
        count = 0
        for num in nums:
            if num == 0:
                count += 1
                if count == 3:
                    return True
        return False

    def threeSumSlow(self, nums: list[int]) -> list[list[int]]:
        '''Slow version of method `threeSum`'''

        positive = [num for num in nums if num >= 0]
        if not positive: return []
        
        threes = []

        if self.__three_zero_exists(positive):
            threes.append([0, 0, 0])
        
        negative = [num for num in nums if num < 0]
        if not negative: return threes

        def pair_combitations(list1: list[int], list2: list[int]):
            for num in list1:
                i1 = i2 = 0
                for i1 in range(len(list2)):
                    for i2 in range(i1 + 1, len(list2)):
                        three = [num, list2[i1], list2[i2]]
                        if sum(three) == 0 and not self.__three_exists(threes, three):
                            threes.append(three)
        
        pair_combitations(positive, negative)
        pair_combitations(negative, positive)
        
        return threes

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        Знаходить в `nums` всі комбінації з трьох чисел, які в сумі дають 0,
        та повертає лист з цими комбінаціями.

        ```
        threeSum([-1,0,1,2,-1,-4]) -> [[-1, -1, 2], [0, -1, 1]]
        
        ```
        '''

        nums.sort()
        threes = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]: continue

            left_i = i + 1
            right_i = len(nums) - 1
            
            while left_i < right_i:
                three_sum = nums[left_i] + nums[i] + nums[right_i]

                if three_sum == 0:
                    threes.append([nums[left_i], nums[i], nums[right_i]])

                    while left_i < right_i and nums[left_i] == nums[left_i + 1]:
                        left_i += 1
                    
                    while left_i < right_i and nums[right_i] == nums[right_i - 1]:
                        right_i -= 1
                    
                    left_i += 1
                    right_i -= 1

                elif three_sum > 0:
                    right_i -= 1
                else:
                    left_i += 1
        
        return threes

s = Solution15()
print(s.threeSum([-1,0,1,2,-1,-4]))