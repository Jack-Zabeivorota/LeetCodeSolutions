from typing import List

class Solution68:
    def __generate_line(self, words: List[str], free_space: int) -> str:
        spaces_coef = free_space / (len(words) - 1)
        spaces = int(spaces_coef)

        if spaces_coef == spaces:
            return (' ' * spaces).join(words)
        
        else_spaces = free_space - spaces * (len(words) - 1)
        return f'{(" " * (spaces + 1)).join(words[:else_spaces])}{" " * (spaces + 1)}{(" " * spaces).join(words[else_spaces:])}'

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        Повертає рядки довжиною `maxWidth` з щільно упакованими в них словами `words`,
        які розтянуті по ширені рядка.

        ```
        fullJustify(["What","must","be","acknowledgment","shall","be"], 16) ->
        [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        ```
        '''

        if not words: return []

        words_len = words_count = start = 0
        result = []

        for i in range(len(words)):
            if words_len + len(words[i]) + words_count <= maxWidth:
                words_len += len(words[i])
                words_count += 1
            else:
                free_space = maxWidth - words_len

                if words_count == 1:
                    result.append(words[start] + (' ' * free_space))
                else:
                    result.append(self.__generate_line(words[start:i], free_space))
                
                start = i
                words_len = len(words[i])
                words_count = 1
        
        free_space = maxWidth - (words_len + words_count - 1)
        result.append(' '.join(words[start:]) + (' ' * free_space))
        
        return result
                

s = Solution68()
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))