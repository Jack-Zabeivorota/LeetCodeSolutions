class Solution2491:
    def dividePlayers(self, skill: list[int]) -> int:
        '''
        Ділить гравців на дві категорії `skill / 2`, та в випадку коли
        всіх гравців з обоїх категорій можно об'єднати попарно так, щоб сума
        навичків кожної пари були рівними, то повертає суму зіграності всіх
        команд, або в іншому випадку `-1`.

        ```
        dividePlayers([3,2,5,1,3,4]) -> (1 * 5) + (2 * 4) + (3 * 3) = 22
        dividePlayers([1,1,2,3]) -> -1

        ```
        '''

        skill.sort()

        skill_sum = skill[0] + skill[-1]
        result = skill[0] * skill[-1]
        l, r = 1, len(skill) - 2

        while l < r:
            if skill[l] + skill[r] != skill_sum:
                return -1
            
            result += skill[l] * skill[r]
        
            l += 1
            r -= 1
        
        return result


s = Solution2491()
print(s.dividePlayers([1,1,2,3]))