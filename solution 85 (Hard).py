class Rect:
    def __init__(self, y: int, x: int, width: int, height: int):
        self.y, self.x = y, x
        self.width, self.height = width, height
    
    @property
    def perimeter(self) -> int: return self.width * self.height

    @property
    def right_x(self) -> int: return self.x + self.width - 1

    def is_included_in_any(self, segments: list[tuple[int, int]]) -> bool:
        for x1, x2 in reversed(segments):
            if x1 <= self.x:
                return self.right_x <= x2
        
        return False

class Solution85:
    def __get_segments(self, matrix: list[list[str]]) -> list[list[tuple[int, int]]]:
        '''Finds all segments in all rows of a `matrix`'''

        rows, columns = len(matrix), len(matrix[0])
        lines = [[] for _ in range(rows)]

        for y in range(rows):
            start = None

            for x in range(columns):
                if start is None and matrix[y][x] == 1:
                    start = x
                elif not start is None and matrix[y][x] == 0:
                    lines[y].append((start, x - 1))
                    start = None
                
            if not start is None:
                lines[y].append((start, columns - 1))
        
        return lines

    def __turn_on_side(self, matrix: list[list[str]]) -> list[list[str]]:
        rows, columns = len(matrix), len(matrix[0])
        matrix_on_side = [[None] * rows for _ in range(columns)]

        for y in range(rows):
            for x in range(columns):
                matrix_on_side[-(x + 1)][y] = matrix[y][x]
        
        return matrix_on_side

    def __get_max_perimeter(self, lines: list[list[tuple[int, int]]]) -> int:
        rects: list[Rect] = []
        temp_rects: set[Rect] = set()

        # rectangles are assembling from segments
        for y, segments in enumerate(lines):
            del_rects: set[Rect] = set()
            add_rects: set[Rect] = set()

            # checking continue rectangle in next lines
            for rect in temp_rects:
                is_find = False

                for x1, x2 in reversed(segments):
                    if x1 <= rect.x:
                        if rect.right_x <= x2:  # if rectangle completely included in segment
                            rect.height += 1
                            is_find = True

                        elif rect.x <= x2:      # or if rectangle partially included in segment
                            width = x2 - rect.x + 1
                            add_rects.add(Rect(rect.y, rect.x, width, rect.height + 1))
                        break
                        
                if not is_find:
                    rects.append(rect)
                    del_rects.add(rect)
            
            temp_rects -= del_rects
            temp_rects.update(add_rects)


            # defining new rectangles
            for x1, x2 in segments:
                if not any(rect.x == x1 and rect.right_x == x2 for rect in temp_rects):
                    temp_rects.add(Rect(y, x1, x2 - x1 + 1, 1))
            
        rects.extend(temp_rects)


        for rect in rects:
            for y in range(rect.y - 1, -1, -1):
                if rect.is_included_in_any(lines[y]):
                    rect.height += 1
                else: break

        return max(map(lambda r: r.perimeter, rects)) if rects else 0

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        '''
        Повертає найбільший периметр прямокутника з одиниць из матриці `matrix`

        ```
        maximalRectangle([
            [1,0,1,0,0],
            [1,0,1,1,1],
            [1,1,1,1,1],
            [1,0,0,1,0]
        ]) -> 6
        ```
        '''

        if not matrix or not matrix[0]: return 0

        lines = self.__get_segments(matrix)
        lines_side = self.__get_segments(self.__turn_on_side(matrix))

        return max(
            self.__get_max_perimeter(lines),
            self.__get_max_perimeter(lines_side)
        )

s = Solution85()

print(s.maximalRectangle([
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0]
]))

print(s.maximalRectangle([
    [1,1,0,1,1,1],
    [0,1,1,1,1,1],
    [1,1,1,1,1,0],
    [1,1,1,1,0,1],
    [1,0,1,1,1,1],
    [1,0,1,1,1,0],
]))

print(s.maximalRectangle([
    [0,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,0],
    [1,1,1,1,0,0],
    [0,1,1,0,0,0],
]))