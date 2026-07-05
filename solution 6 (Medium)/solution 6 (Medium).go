package main

import (
	"slices"
)

/*
Рядок `word` записується зигзагоподібним візерунком на рядках
кількості `numRows` штук. Функція повертає ці рядки об'єднані в один.

	convert("ABCDCBABCD---", 4) -> "AA-BBB-CCC-DD"
	// row 1: A     A       -
	// row 2:  B   B  B    -
	// row 3:   C C    C  -
	// row 4:    D      D
*/
func convert(word string, numRows int) string {
	if numRows == 1 {
		return word
	}
	rows := make([][]rune, numRows)

	for i := range rows {
		rows[i] = make([]rune, 0, 100)
	}

	isToDown := true
	i := 0

	for _, c := range word {
		// add char
		rows[i] = append(rows[i], c)

		// change direction
		if isToDown && i == len(rows)-1 {
			isToDown = false
		}
		if !isToDown && i == 0 {
			isToDown = true
		}

		// next row
		if isToDown {
			i++
		} else {
			i--
		}
	}

	return string(slices.Concat(rows...))
}

func main() {
	println(convert("ABCDCBABCD---", 4))
}
