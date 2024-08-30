from collections import Counter

class Solution1001:
    def __is_illuminated(self, lamp: tuple[int, int]) -> int:
        y, x = lamp
        
        if y in self.horizontals or x in self.verticals:
            return 1

        if x - y in self.left_diagonal or self.n - 1 - x - y in self.right_diagonal:
            return 1

        return 0

    def __remove_ligths_from_range(self, lights: set[tuple[int, int]], position: tuple[int, int], n: int):
        y, x = position

        positions = (
            #  column 1      column 2      column 3
            (y - 1, x - 1), (y - 1, x), (y - 1, x + 1), # row 1
            (y,     x - 1), (y,     x), (y,     x + 1), # row 2
            (y + 1, x - 1), (y + 1, x), (y + 1, x + 1), # row 3
        )
        
        for pos in positions:
            if pos in lights:
                lights.remove(pos)

                y, x = pos
                ld, rd = x - y, self.n - 1 - x - y

                self.horizontals[y] -= 1
                if self.horizontals[y] == 0: self.horizontals.pop(y)

                self.verticals[x] -= 1
                if self.verticals[x] == 0: self.verticals.pop(x)

                self.left_diagonal[ld] -= 1
                if self.left_diagonal[ld] == 0: self.left_diagonal.pop(ld)

                self.right_diagonal[rd] -= 1
                if self.right_diagonal[rd] == 0: self.right_diagonal.pop(rd)

    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        '''
        Є сітка розміром `n * n` клітинок, на ній розташовані лампи, позиції яких указані
        в `lamps` (`[row,col]`). Лампи освітлюють свою вертикаль, горизонталь та діагоналі
        відносно позиції лампи. В `queries` указані 
        
        (`0 <= n <= 1_000_000_000`)

        (`0 <= len(lamps) <= 20_000`)

        (`0 <= len(queries) <= 20_000`)

        Функція повертає стани освітлення по позиціям вказаних в `queries`, 1 якщо освітлена, інакше 0.
        (Після перевірки освітлення позиції, всі лампи в радіусі одной клітинки вимикаються)

        ```
        gridIllumination(5, [[0,0],[0,4]], [[0,4],[0,1],[1,4]]) -> [1,1,0]
        
        ```
        '''

        lights = set(map(tuple, lamps))

        self.horizontals, self.verticals = Counter(), Counter()
        self.left_diagonal, self.right_diagonal = Counter(), Counter()
        self.n = n

        for y, x in lights:
            self.horizontals[y] += 1
            self.verticals[x] += 1
            self.left_diagonal[x - y] += 1
            self.right_diagonal[n - 1 - x - y] += 1

        ans = []

        for lamp in queries:
            ans.append(self.__is_illuminated(lamp))
            self.__remove_ligths_from_range(lights, lamp)
        
        return ans

s = Solution1001()
print(s.gridIllumination(5, [[0,0],[0,4]], [[0,4],[0,1],[1,4]]))