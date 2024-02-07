class Solution:
    def reverse(self, x: int) -> int:
        '''
        Повертає перевернуте число `x`.
        ```
        reverse(-4587) -> -7854
        ```
        '''

        x_str = str(x)

        if len(x_str) == 1:
            return x

        x = int(x_str[::-1]) if x > 0 else 0 - int(x_str[:0:-1])
        
        return x if -2147483648 <= x <= 2147483647 else 0

s = Solution()
print(s.reverse(-123))