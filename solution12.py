class Solution:
    def isNumber(self, s: str) -> bool:
        '''
        Повертає `True`, якщо `s` являється числом.
        ```
        isNumber('123') -> True
        isNumber('-89.546') -> True
        isNumber('.27') -> True
        isNumber('+5.e3') -> True

        ```
        '''

        if s in ('', '+', '-', '.'):
            return False

        is_find_dot = is_find_e = False

        if not s[0].isdigit() and not s[0] in ('+', '-'):
            if s[0] == '.' and s[1].isdigit():
                is_find_dot = True
            else:
                return False
        
        i = 1
        while i < len(s):
            if not s[i].isdigit():

                # check dot
                if (not is_find_dot and not is_find_e and s[i] == '.'
                    and (s[i - 1].isdigit() or (i < len(s) - 1 and s[i + 1].isdigit()))
                ):
                    is_find_dot = True

                # check E
                elif not is_find_e and s[i] in ('e', 'E') and (s[i - 1].isdigit() or s[i - 1] == '.'):

                    if i < len(s) - 1 and s[i + 1].isdigit():
                        is_find_e = True
                        i += 1

                    elif i < len(s) - 2 and s[i + 1] in ('+', '-') and s[i + 2].isdigit():
                        is_find_e = True
                        i += 2

                    else:
                        return False
                
                else:
                    return False
            
            i += 1
        
        return True

s = Solution()
print(s.isNumber('+5.e3'))