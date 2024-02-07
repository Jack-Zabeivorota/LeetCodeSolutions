class Solution:
    def lengthOfLongestSubstring(self, source: str) -> int:
        '''
        Повертає довжину найбільшого підрядка в `source`, символи якого не повторюються.
        ```
        lengthOfLongestSubstring('abacabde') -> 'cabde'
        ```
        '''

        substring_max_len = last_chars_len = chars_len = i = 0
        source_len = len(source)
        chars = set()

        while i < source_len:
            chars.add(source[i])
            chars_len = len(chars)

            if chars_len == last_chars_len:
                if chars_len > substring_max_len:
                    substring_max_len = chars_len
                i -= chars_len
                chars.clear()
                last_chars_len = 0
            else:
                last_chars_len += 1

            i += 1
            
        return max(substring_max_len, chars_len)
    
s = Solution()
print(s.lengthOfLongestSubstring('dhsdfge'))