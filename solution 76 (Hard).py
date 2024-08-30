from collections import Counter, deque

class Solution76:
    def __decrese_and_del_zero(self, count: Counter, key):
        if count[key] > 1:
            count[key] -= 1
        else:
            count.pop(key)

    def minWindow(self, source: str, chars: str) -> str:
        '''
        Повертає найменший підрядок з `source`, який містить всі символи `chars`

        ```
        s.minWindow("ADAOBECODBEANCBG", "ABBC") -> 'BEANCB'
        
        ```
        '''

        if not source or not chars or len(source) < len(chars):
            return ''

        min_substr = ''
        chars_count = Counter(chars)
        positions = {c: deque() for c in chars_count}
        start = None

        for i, char in enumerate(source):
            if char in positions:
                positions[char].append(i)

                if char in chars_count:
                    self.__decrese_and_del_zero(chars_count, char)
                else:
                    index = positions[char].popleft()
                    if index == start: start = None

                if not chars_count:
                    if start is None:
                        start = min(deq[0] for deq in positions.values())

                    if not min_substr or i - start + 1 < len(min_substr):
                        min_substr = source[start : i + 1]
        
        return min_substr


s = Solution76()
print(s.minWindow("ADAOBECODBEANCBG", "ABBC"))