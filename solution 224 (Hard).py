class Solution224:
    def calc(self, index: int = 0) -> tuple[int, int]:
        i = index
        str_num = []
        num = None
        is_plus = True
        result = None

        def operate():
            nonlocal result, num

            if str_num:
                num = int(''.join(str_num))
                str_num.clear()
                
            if not num is None:
                if result is None:
                    if not is_plus: num = -num
                    result = num
                else:
                    result = result + num if is_plus else result - num
                
                num = None


        while True:
            if i == len(self.expression):
                operate()
                return result, i

            char = self.expression[i]

            if char == ')':
                operate()
                return result, i

            if char.isdigit():
                str_num.append(char)

            elif char in ('-', '+'):
                operate()
                is_plus = char == '+'
            
            elif char == '(':
                num, i = self.calc(i + 1)
        
            i += 1

    def calculate(self, expression: str) -> int:
        '''
        Обчислює математичне вираження `expression` та повертає результат.

        ```
        calculate('  5+ 3 -(-2+0 )') -> 10

        ```
        '''

        self.expression = expression
        result, _ = self.calc()
        return result


s = Solution224()
print(s.calculate('(3-(5-(8)-(2+(9-(0-(8-(2))))-(4))-(4)))')) # -> 23
print(s.calculate('- (3 + (4 + 5))')) # -> -12