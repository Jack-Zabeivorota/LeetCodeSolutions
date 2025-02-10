package main

import "sort"

type CharWeight struct {
	Char   byte
	Level  int
	Weight int
}

/*
Повертає алфавіт, по якому розташовані слова в `words`

	alienDict([]string{"ad", "ba", "cb", "cb", "cde"}) -> "abcd"
*/
func alienDict(words []string) string {
	// find the weight of chars

	firstChar := words[0][0]
	findedChars := map[byte]bool{firstChar: true}
	charWeights := []CharWeight{{Char: firstChar, Level: 0, Weight: 0}}
	weight := 1

	for i := 0; i < len(words)-1; i++ {
		word1, word2 := words[i], words[i+1]

		for lvl := 0; lvl < len(word1); lvl++ {
			char1, char2 := word1[lvl], word2[lvl]

			if _, ok := findedChars[char2]; !ok && char1 != char2 {
				findedChars[char2] = true
				charWeights = append(charWeights, CharWeight{
					Char:   char2,
					Level:  lvl,
					Weight: weight,
				})
				weight++
				break
			}
		}
	}

	// sort weight chars first by level, then by weight

	sort.Slice(charWeights, func(i, j int) bool {
		if charWeights[i].Level != charWeights[j].Level {
			return charWeights[i].Level < charWeights[j].Level
		}
		return charWeights[i].Weight < charWeights[j].Weight
	})

	// forming the alphabet

	alphabet := make([]byte, len(charWeights))

	for i, cw := range charWeights {
		alphabet[i] = cw.Char
	}

	return string(alphabet)
}

func main() {
	println(alienDict([]string{"wrt", "wrf", "er", "ett", "rftt"}))
}
