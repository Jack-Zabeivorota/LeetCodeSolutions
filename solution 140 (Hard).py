class WordVariator:
    def __init__(self, word: str, index: int, words: dict[int, list[str]], string_len: int, collector: list, prev_variator = None):
        self.word = word
        self.prev_variator = prev_variator
        index += len(word)

        if index < string_len:
            if not index in words: return

            for w in words[index]:
                WordVariator(w, index, words, string_len, collector, self)
        else:
            collector.append(self)

class Solution140:
    def wordBreak(self, string: str, word_dict: list[str]) -> list[str]:
        '''
        Повертає всі варіанти реченнь із `string`, всі розділені
        пробілами слова якого можна знайти в списку `word_dict`.

        ```
        wordBreak("catsanddog", ["cats","dog","sand","and","cat"]) -> ["cats and dog", "cat sand dog"]
        
        ```
        '''

        # find all word possitions at string

        words: dict[int, list[str]] = {}

        for word in word_dict:
            index: int = 0

            while True:
                index = string.find(word, index)
                if index == -1: break

                if not index in words:
                    words[index] = []

                words[index].append(word)
                index += 1

        
        # building trees of possible word sequences

        strings: list[str] = []
        collector: list[WordVariator] = []

        if 0 in words:
            for word in words[0]:
                WordVariator(word, 0, words, len(string), collector)
        
        for variator in collector:
            string_parts: list[str] = []

            while not variator is None:
                string_parts.append(variator.word)
                variator = variator.prev_variator
            
            string_parts.reverse()
            strings.append(' '.join(string_parts))
        
        return strings

s = Solution140()
print(s.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))