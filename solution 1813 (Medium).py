class Solution1813:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        '''
        Повертає `True`, якщо `sentence1` i `sentence2` подібні, тобто коли можно
        вставити довільне речення (розділене пробілами) з одного рядка в другий i
        вони стануть рівними, інакше повертає `False`.
        
        ```
        # Hello > my name is < Jane
        areSentencesSimilar('Hello Jane', 'Hello my name is Jane') -> True

        # Частина "s are" не розділена пробілами
        areSentencesSimilar('Frog cool', 'Frogs are cool') -> False


        ```
        '''

        if sentence1 == sentence2 or '' in (sentence1, sentence2):
            return True
        
        sen, source = (sentence1, sentence2) if len(sentence1) < len(sentence2) else (sentence2, sentence1)
        sen_words, source_words = sen.split(' '), source.split(' ')

        start, end = -1, len(sen_words)

        for i in range(len(sen_words)):
            if sen_words[i] == source_words[i]:
                start += 1
            else: break

        
        for i in range(1, len(sen_words) + 1):
            if sen_words[-i] == source_words[-i]:
                end -= 1
            else: break
        
        return start == len(sen) - 1 or end == 0 or start + 1 >= end


s = Solution1813()
print(s.areSentencesSimilar('My name is Haley', 'My Haley'))
print(s.areSentencesSimilar('a b a b b c', 'a b c'))