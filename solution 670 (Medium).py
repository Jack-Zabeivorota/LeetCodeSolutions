class Solution670:
    def maximumSwap(self, num: int) -> int:
        '''
        Повертає максимальне число, яке можно відтворити з числа `num`,
        один раз помінявши в ньому містами дві цифри. Якщо більшого
        ніж `num` числа відтворити не можна, то повертає `num`.

        ```
        maximumSwap(1993) -> 9913
        #           - -

        ```
        '''

        digits = list(int(c) for c in str(num))

        for i in range(len(digits)):
            if digits[i] == 9:
                continue

            index = i

            for j in range(i + 1, len(digits)):
                if (index == i and digits[j] > digits[index] or
                    index > i and digits[j] >= digits[index]):
                    index = j
            
            if index > i:
                digits[i], digits[index] = digits[index], digits[i]
                return int(''.join(str(d) for d in digits))

        return num


s = Solution670()
print(s.maximumSwap(98368)) # -> 98863