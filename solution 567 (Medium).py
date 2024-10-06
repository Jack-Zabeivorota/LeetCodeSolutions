from collections import Counter


class Solution567:
    def checkInclusionSlow(self, s1: str, s2: str) -> bool:
        '''Slow version of checkInclusion'''

        if len(s1) > len(s2) or len(s1) == 0:
            return False

        s1_sum, s1_product = 0, 1

        for c in s1:
            num = ord(c) - 96
            s1_sum += num
            s1_product *= num
        
        chars = set(s1)
        loc_sum = count = i = 0
        loc_product = 1

        while i < len(s2):
            if s2[i] in chars:
                num = ord(s2[i]) - 96
                loc_sum += num
                loc_product *= num
                count += 1

                if count == len(s1):
                    if loc_sum == s1_sum and loc_product == s1_product:
                        return True
                    
                    i -= count - 1
                    loc_sum = count = 0
                    loc_product = 1
            else:
                loc_sum = count = 0
                loc_product = 1
            
            i += 1

        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Повертає `True`, якщо рядок `s1` в довільному порядку
        символів входить в `s2`, інакше `False`.
        
        ```
        checkInclusion('abc', 'evbcag') -> True # ev[bca]g
        checkInclusion('ab', 'bbcaa') -> False

        ```
        '''

        if len(s1) > len(s2) or len(s1) == 0:
            return False
        
        count1, count2 = Counter(s1), Counter(s2[:len(s1)])

        if count1 == count2:
            return True

        l, r = 1, len(s1)

        while r < len(s2):
            prev_char = s2[l - 1]

            if count2[prev_char] > 0:
                count2[prev_char] -= 1
            else:
                del count2[prev_char]

            count2[s2[r]] += 1

            if count1 == count2:
                return True
            
            r += 1
            l += 1

        return False


s = Solution567()
print(s.checkInclusion('abc', 'ccccbbbbaaaa'))