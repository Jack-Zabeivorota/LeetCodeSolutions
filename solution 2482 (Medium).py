class Solution2482:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        '''
        Повертає матрицю того ж розміру, що і матриця `grid`, кожен елемент якої
        дорівнює сумі всіх значень з рядку і колонки матриці `grid`,
        на перехресті якого знаходиться елемент, де 1 = +1, а 0 = -1.

        ```
        [0, 1, 1],    [ 0, 0, 4],
        [1, 0, 1], -> [ 0, 0, 4],
        [0, 0, 1]     [-2,-2, 2]
        ```
        '''

        if not grid: return []

        rowCount, colCount = {}, {}

        for y in range(len(grid)): rowCount[y] = 0

        for x in range(len(grid[0])): colCount[x] = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    rowCount[y] += 1
                    colCount[x] += 1
                else:
                    rowCount[y] -= 1
                    colCount[x] -= 1

        diffGrid = []

        for y in range(len(grid)):
            diffGrid.append([])
            for x in range(len(grid[y])):
                diffGrid[y].append(rowCount[y] + colCount[x])
        
        return diffGrid

s = Solution2482()
print(s.onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))