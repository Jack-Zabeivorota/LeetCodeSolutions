class Solution1963:
    def _rindex(self, arr: list, val, end: int) -> int:
        i = end - 1

        while i >= 0:
            if arr[i] == val:
                return i
            i -= 1
        
        return -1

    def minSwaps(self, s: str) -> int:
        '''
        Повертає мінімальну кількість перестановок квадратних дужок в рядку `s`,
        так щоб рядок був сбалансованим/корректним.

        Рядок `s` парний (`len(s) % 2 == 0`), містить лише квадратні дужки (`[`, `]`),
        кількість відкритих та закритих дужок в рядку однакова.

        ```
        minSwaps(']]][[[')   -> 2 # [[][]]
        minSwaps(']][[[]][') -> 1 # [][[[]]]

        ```
        '''


        brs = list(s)
        opens = replaces = 0
        b_idx = len(brs)

        for i in range(len(brs)):
            if brs[i] == '[':
                opens += 1
            elif opens > 0:
                opens -= 1
            else:
                b_idx = self._rindex(brs, '[', b_idx)
                brs[i], brs[b_idx] = brs[b_idx], brs[i]
                replaces += 1
                opens += 1

        print(''.join(brs))
        return replaces



s = Solution1963()
print(s.minSwaps('[]][[]'))