from collections import Counter


class Line:
    def __init__(self, point1: tuple[int, int], point2: tuple[int, int]):
        self._point1 = point1
        self._point2 = point2
        self._points = [point1, point2]
    
    def get_len(self) -> int:
        return len(self._points)

    def is_included(self, point: tuple[int, int]) -> bool:
        x1, y1 = self._point1
        x2, y2 = self._point2
        x3, y3 = point

        return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0

    def add_point(self, point: tuple[int, int]) -> bool:
        if self.is_included(point):
            self._points.append(point)
            return True
        
        return False

    def set_points_in(self, buff: set[tuple[int, int]]):
        buff.update(self._points)

class Solution149:
    def maxPointsSlow(self, points: list[list[int]]) -> int:
        '''Slow version of method `maxPoints`'''
        
        if len(points) < 2:
            return len(points)

        points: list[tuple[int, int]] = [tuple(p) for p in points]
        lines: list[Line] = []
        max_len = 2

        for i, point in enumerate(points):
            _points: set[tuple[int, int]] = set()

            for line in lines:
                if line.add_point(point):
                    max_len = max(max_len, line.get_len())
                    line.set_points_in(_points)

            for j in range(i):
                if not points[j] in _points:
                    lines.append(Line(points[j], point))
        
        return max_len

    def maxPoints(self, points: list[list[int]]) -> int:
        '''
        Повертає найбільшу кількість точок, які лежать на одній прямій лінії,
        побудованій по точкам `points`.

        ```
        ' 3| . . o . . '
        ' 2| . o . . o '
        ' 1| o . . . . '
        '   -----------'
        '    1 2 3 4 5  '
        '              '
        maxPoints([[1,1],[2,2],[2,5],[3,3]) -> 3
        ```
        '''

        max_len = 0

        for x1, y1 in points:
            vectors = []

            for x2, y2 in points:
                if x1 == x2 and y1 == y2: continue

                x_delta, y_delta = x1 - x2, y1 - y2
                vectors.append(x_delta / y_delta if y_delta != 0 else float('inf'))
            
            loc_max_len = max(Counter(vectors).values() or [0]) + 1
            max_len = max(max_len, loc_max_len)

        return max_len

s = Solution149()
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])) # 4
print(s.maxPoints([[1,0],[0,0]])) # 2