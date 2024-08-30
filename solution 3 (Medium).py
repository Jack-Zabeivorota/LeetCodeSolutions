class Solution3:
    def lengthOfLongestSubstring(self, source: str) -> int:
        '''
        Повертає довжину найбільшого підрядка в `source`, символи якого не повторюються.

        ```
        lengthOfLongestSubstring('abacabde') -> 'cabde'

        ```
        '''

        max_len = last_chars_len = chars_len = i = 0
        chars = set()

        while i < len(source):
            chars.add(source[i])
            chars_len = len(chars)

            if chars_len == last_chars_len:
                max_len = max(max_len, chars_len)
                i -= chars_len
                chars.clear()
                last_chars_len = 0
            else:
                last_chars_len += 1

            i += 1
            
        return max(max_len, chars_len)
    
s = Solution3()
print(s.lengthOfLongestSubstring('dhsdfge'))