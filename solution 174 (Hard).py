class State:
    def __init__(self, y: int, x: int, healt: int, healt_drawdown: int):
        self.y = y
        self.x = x
        self.healt = healt
        self.healt_drawdown = healt_drawdown

class Solution174:
    def is_target(self, y: int, x: int) -> bool:
        return y + 1 == self.height and x + 1 == self.width

    def throw_state(self, y: int, x: int, healt: int, healt_drawdown: int):
        if self.is_target(y, x):
            self.healt_drawdowns.append(healt_drawdown)
            return

        def add_state(new_y: int, new_x: int):
            new_healt = healt + self.get_damage(new_y, new_x)
            self.throw_state(new_y, new_x, new_healt, min(healt_drawdown, new_healt))

        if y + 1 < self.height:
            add_state(y + 1, x)

        if x + 1 < self.width:
            add_state(y, x + 1)

    def calculateMinimumHPSlow(self, dungeon: list[list[int]]) -> int:
        '''Slow version of method `calculateMinimumHP`'''
        
        self.width = len(dungeon[0])
        self.height = len(dungeon)
        self.healt_drawdowns = []
        self.get_damage = lambda y, x: dungeon[y][x]
        
        healt = dungeon[0][0]
        self.throw_state(0, 0, healt, min(0, healt))
    
        return -max(self.healt_drawdowns) + 1


    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        '''
        Повертає мінімальну кількість здров'я героя, необхідного для проходження карти `dungeon`.

        Герой знаходиться в лівому верхньому кутку карти, а принцеса в правому нижньому кутку.
        Герою потрібно дістатися до принцеси ідучи тільки вліво або вниз по карті. На кожному
        кроці герой може втрачати або збільшувати кількість свого здоров'я. Якщо здоров'я героя
        дійде по нуля, то гра завершується.

        ```
        calculateMinimumHP([
            [-2,  -3,  3],
            [-5, -10,  1],
            [ 10, 30, -5]
        ]) -> 7

        # Кроки (Здоров'я): start (7) -> -2 (5) -> -3 (2) -> 3 (5) -> 1 (6) -> -5 (1)
        
        ```
        '''

        height = len(dungeon)
        width = len(dungeon[0])

        # create damage map

        dp = [None] * height

        for y in range(height):
            dp[y] = [None] * width

        def set_damage_in_dp(y: int, x: int, curr_damage: int):
            curr_damage += dungeon[y][x]
            dp[y][x] = curr_damage if curr_damage < 0 else 0

        # set damage for the last row of the map

        set_damage_in_dp(-1, -1, 0)

        for x in range(width-2, -1, -1):
            set_damage_in_dp(-1, x, dp[-1][x+1])

        # set damage to other map cells

        for y in range(height-2, -1, -1):
            set_damage_in_dp(y, -1, dp[y+1][-1])

            for x in range(width-2, -1, -1):
                set_damage_in_dp(y, x, max(dp[y][x+1], dp[y+1][x]))
    

        return -dp[0][0] + 1


s = Solution174()
print(s.calculateMinimumHP([
    [-2,  -3,  3],
    [-5, -10,  1],
    [ 10, 30, -5]
]))

print(s.calculateMinimumHP([
    [ -2,  -3,  3],
    [ -3, -10,  1],
    [-10, -30, -5]
]))