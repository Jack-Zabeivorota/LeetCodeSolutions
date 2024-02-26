from typing import List

class Solution42:
    def trap_slow(self, heights: List[int]) -> int:
        'Slow version of `trap`'

        max_height = max(heights)
        wather_count = 0

        for level in range(1, max_height + 1):
            left_barier_idx = None

            for i in range(len(heights)):
                if heights[i] >= level:
                    if left_barier_idx is None:
                        left_barier_idx = i
                        continue
                    
                    wather_count += i - left_barier_idx - 1
                    left_barier_idx = i
                    
        return wather_count

    def trap(self, heights: List[int]) -> int:
        '''
        Повертає кількість води яка залишиться після дощу на рельєфі з вершинами `heights`.
        ```
        m - block
        ; - wather

        3|       m
        2|   m;;;mm;m
        1| m;mm;mmmmmm;m

        trap([0,1,0,2,1,0,1,3,2,1,2,1,0,1]) -> 7
        ```
        '''

        counter = 0
        ledges = []

        for i in range(1, len(heights)):
            if heights[i - 1] < heights[i]:
                delta = heights[i] - heights[i - 1]

                while ledges:
                    ledge = ledges[-1]

                    if ledge['delta'] > delta:
                        counter += (i - ledge['index']) * delta
                        ledge['delta'] -= delta
                        break
                    else:
                        counter += (i - ledge['index']) * ledge['delta']
                        delta -= ledge['delta']
                        ledges.pop()

                        if delta == 0: break

            elif heights[i - 1] > heights[i]:
                ledges.append({
                    'index': i,
                    'delta': heights[i - 1] - heights[i],
                })
        
        return counter
            

s = Solution42()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1,0,1]))