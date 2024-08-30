class Solution32:
    def longestValidParentheses(self, source: str) -> int:
        '''
        Повертає число, яке відповідає найдовшому підрядку із рядка `source`,
        в якому всі дужки вистрояні корректно.
        
        ```
        longestValidParentheses('(()') -> 2
        longestValidParentheses('(()((()())') -> 6
        ```
        '''

        sequence = [False for _ in source]
        opened = []

        for i in range(len(source)):
            if source[i] == '(':
                opened.append(i)
            elif source[i] == ')' and opened:
                sequence[opened[-1]] = True
                sequence[i] = True
                opened.pop()
        
        max_count = count = 0

        for val in sequence:
            if val:
                count += 1
            else:
                if count > max_count: max_count = count
                count = 0
        
        return max(max_count, count)

s = Solution32()
print(s.longestValidParentheses('(()((()())'))