class Solution214:
    def is_palindrome(self, start: int, end: int, source: str) -> bool:
        while start < end:
            if source[start] != source[end]:
                return False
            
            start += 1
            end -= 1
        
        return True

    def shortestPalindrome(self, source: str) -> str:
        '''
        Доповнює рядок `source` символи таким чином, щоб сформувався найкоротший
        паліндром та повертає результат.

        ```
        shortestPalindrome('aaabb') -> 'bbaaabb'

        ```
        '''

        if not source:
            return ''

        max_pldr_len, side = 1, -1

        for i in range(1, len(source)):
            # check palindrome from left side
            pldr_len = i + 1

            if pldr_len > max_pldr_len and self.is_palindrome(0, i, source):
                max_pldr_len, side = pldr_len, -1
            
            # check palindrome from right side
            pldr_len = len(source) - i

            if pldr_len > max_pldr_len and self.is_palindrome(i, len(source) - 1, source):
                max_pldr_len, side = pldr_len, 1
        

        if side == -1:
            return source[max_pldr_len:][::-1] + source
        
        return source + source[: len(source) - max_pldr_len][::-1]


s = Solution214()

print(s.shortestPalindrome('aacecaaa')) # -> aaacecaaa
print(s.shortestPalindrome('ghabab'))   # -> ghababgh
print(s.shortestPalindrome('abcd'))     # -> dcbabcd
