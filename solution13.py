class Solution:
    def lengthOfLongestSubstring(self, source: str) -> int:
        '''
        Повертає довжину найбільшого підрядка в `source`, символи якого не повторюються.
        ```
        lengthOfLongestSubstring('abacabde') -> 'cabde'
        ```
        '''

        substring_max_len = last_chars_len = i = 0
        chars = set()

        while i < len(source):
            chars.add(source[i])

            if len(chars) == last_chars_len:
                if len(chars) > substring_max_len:
                    substring_max_len = len(chars)
                i -= len(chars)
                chars.clear()
                last_chars_len = 0
            else:
                last_chars_len += 1

            i += 1
            
        return max(substring_max_len, len(chars))
    
s = Solution()
print(s.lengthOfLongestSubstring('dhsdfge'))