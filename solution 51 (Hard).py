from typing import List

class QueenVariator:
    def __init__(self, chessboard: List[List[str | None]], queen_x: int, collector: List, prev_variator = None):
        self.prev_variator = prev_variator
        self.__chessboard = chessboard
        self.__set_queen_on_chessboard(queen_x)
        
        if len(chessboard) > 1:
            self.__generate_variators(collector)
        else:
            collector.append(self)
    
    def __generate_variators(self, collector: List):
        for x in range(len(self.__chessboard[0])):
            if self.__chessboard[1][x] is None:
                chessboard = [self.__chessboard[i].copy() for i in range(1, len(self.__chessboard))]
                QueenVariator(chessboard, x, collector, self)

    def __set_queen_on_chessboard(self, x: int):
        row_len = len(self.__chessboard[0])

        self.__chessboard[0] = ['.'] * row_len
        self.__chessboard[0][x] = 'Q'

        shift = 1

        for y in range(1, len(self.__chessboard)):
            self.__chessboard[y][x] = '.'

            if x - shift > -1:
                self.__chessboard[y][x - shift] = '.'
            
            if x + shift < row_len:
                self.__chessboard[y][x + shift] = '.'

            shift += 1

    @property
    def first_row(self): return self.__chessboard[0]

    @staticmethod
    def get_variants(variators: List):
        if not variators: return []

        chessboards = []
        n = len(variators[0].first_row)

        for variator in variators:
            chessboard = [None] * n
            i = n - 1

            while variator:
                chessboard[i] = ''.join(variator.first_row)
                variator = variator.prev_variator
                i -= 1
            
            chessboards.append(chessboard)
        
        return chessboards

class Solution51:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        Повертає всі конфігурації з `n` дамок на дошці `n * n`,
        в якому жодна дамка не атакує другу дамку

        ```
        solveNQueens(4) -> [
            ['.Q..',  ['..Q.',
             '...Q',   'Q...',
             'Q...',   '...Q',
             '..Q.'],  '.Q..']
        ]
        ```
        '''

        if n in (0, 2, 3): return []
        if n == 1: return [['Q']]

        collector = []

        for x in range(n):
            QueenVariator([[None] * n for _ in range(n)], x, collector)

        return QueenVariator.get_variants(collector)


s = Solution51()
print(s.solveNQueens(5))