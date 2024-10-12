class Solution2406:
    def minGroupsSlow(self, intervals: list[list[int]]) -> int:
        '''Slow version of minGroups'''

        intervals.sort(key=lambda x: x[0])

        groups: list[list[int]] = []
        
        for intv in intervals:
            for i in range(len(groups)):
                if groups[i][1] < intv[0]:
                    groups[i] = intv
                    break
            else:
                groups.append(intv)
        
        return len(groups)

    def minGroups(self, intervals: list[list[int]]) -> int:
        '''
        Повертає мінімальну кількість груп, на які можна поділити
        `intervals`, так щоб всі інтервали в групі не перетиналися.

        ```
        minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]) -> 3
        
        # group 1: [1,5], [6,8]
        # group 2: [1,10]
        # group 3: [2,3], [5,10]

        ```
        '''

        starts = sorted(intv[0] for intv in intervals)
        ends   = sorted(intv[1] for intv in intervals)
        end_idx = groups = 0

        for start in starts:
            if start > ends[end_idx]:
                end_idx += 1
            else:
                groups += 1

        return groups


s = Solution2406()
print(s.minGroups([[1,3],[5,8],[10,15],[7,12]]))