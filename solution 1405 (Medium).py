class Solution1405:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        '''
        Повертає найдовший рядок, який складається з символів 'a', 'b' i 'c',
        кількість яких не перевищує числа `a`, `b` i `c` відповідно, та
        кожен з символів не повторюється більше 2-x разів підряд.

        ```
        longestDiverseString(1, 1, 7) -> ccaccbcc

        ```
        '''

        chars = sorted((['a',a], ['b',b], ['c',c]), key=lambda x: x[1])
        firsts_sum = sum(chars[i][1] for i in range(len(chars)-1))

        if chars[-1][1] / 2 - 1 > firsts_sum:
            chars[-1][1] -= -(2 * firsts_sum) + chars[-1][1] - 2


        sequence = [{chars[-1][0]: 1} for _ in range(chars[-1][1])]
        char_idx = len(chars) - 2

        def add_to_sequence(i: int):
            nonlocal char_idx

            while chars[char_idx][1] == 0:
                if char_idx > 0:
                    char_idx -= 1
                else:
                    return False
            
            letter = chars[char_idx][0]

            if letter in sequence[i]:
                sequence[i][letter] += 1
            else:
                sequence[i][letter] = 1

            chars[char_idx][1] -= 1
            return True

        def get_result():
            string = []

            for node in sequence:
                for letter, count in node.items():
                    string.append(letter * count)
            
            return ''.join(string)
        
        i = start = 1

        while True:
            if not add_to_sequence(i):
                return get_result()

            i += 2

            if i >= len(sequence):
                start = 1 if start == 0 else 0
                i = start


s = Solution1405()
print(s.longestDiverseString(5, 10, 30)) # -> ccbccbccbccbccbccbccbccbccbccbccaccaccaccacca