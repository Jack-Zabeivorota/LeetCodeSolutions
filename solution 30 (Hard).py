from typing import List, Dict

class Solution30:
    def __check_sequence(self, string: str, index: int, word_counts: Dict[str, int]):
        i = index
        end = i + self.sequence_len
        word_counts = word_counts.copy()

        while i < end:
            word = string[i:i + self.word_len]

            if word in word_counts:
                word_counts[word] -= 1
                if word_counts[word] == 0:
                    word_counts.pop(word)
            else: return False
            
            i += self.word_len
        
        return True

    def findSubstring(self, string: str, words: List[str]) -> List[int]:
        '''
        Повертає лист з індексами входження всіх підрядків в рядку `string`,
        в яких присутні всі слова вказані в `words` в любому порядку і без повторів.
        Слова в `words` повинні бути одної довжини.
        ```
        findSubstring('wordgoodgoodgoodbestword', ["word","good","best","good"]) -> [8]
        ```
        '''

        if not string or not words: return []
        
        self.word_len = len(words[0])
        self.sequence_len = self.word_len * len(words)
        valid_string_len = len(string) - self.sequence_len
        word_counts = {}

        for word in words:
            if not word in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1

        finded_sequences = []

        i = 0
        while i <= valid_string_len:
            if self.__check_sequence(string, i, word_counts):
                finded_sequences.append(i)
            i += 1
        
        return finded_sequences

s = Solution30()
print(s.findSubstring('wordgoodgoodgoodbestword', ["word","good","best","good"]))