class Solution4:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        '''
        Повертає медіану листів `nums1` і `nums2`.
        
        ```
        findMedianSortedArrays([1,3], [2,8]) -> 2.5
        
        ```
        '''

        merge_nums = sorted(nums1 + nums2)

        index = len(merge_nums) // 2

        if len(merge_nums) % 2 == 0:
            return (merge_nums[index - 1] + merge_nums[index]) / 2
        else:
            return float(merge_nums[index])
        

s = Solution4()
print(s.findMedianSortedArrays([1,3], [2,8]))