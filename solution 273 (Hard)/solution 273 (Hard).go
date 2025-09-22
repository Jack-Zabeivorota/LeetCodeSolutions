package main

import (
	"strconv"
	"strings"
)

var numbers = map[int]string{
	1:  "One",
	2:  "Two",
	3:  "Three",
	4:  "Four",
	5:  "Five",
	6:  "Six",
	7:  "Seven",
	8:  "Eight",
	9:  "Nine",
	10: "Ten",
	11: "Eleven",
	12: "Twelve",
	13: "Thirteen",
	14: "Fourteen",
	15: "Fifteen",
	16: "Sixteen",
	17: "Seventeen",
	18: "Eighteen",
	19: "Nineteen",
}

var tens = map[int]string{
	1: "Ten",
	2: "Twenty",
	3: "Thirty",
	4: "Forty",
	5: "Fifty",
	6: "Sixty",
	7: "Seventy",
	8: "Eighty",
	9: "Ninety",
}

var classes = map[int]string{
	1: "Hundred",
	2: "Thousand",
	3: "Million",
	4: "Billion",
	5: "Trillion",
	6: "Quadrillion",
	7: "Quintillion",
}

func classToWords(class string, index int) []string {
	if class == "000" {
		return []string{}
	}

	result := []string{}
	n := 0

	// Find hundreds

	if class[0] != '0' {
		n = int(class[0] - 48)
		result = append(result, numbers[n], classes[1])
	}

	// Find tens and numbers

	n, _ = strconv.Atoi(class[1:])

	if n > 0 {
		if n < 20 {
			result = append(result, numbers[n])
		} else {
			t := int(class[1] - 48)
			result = append(result, tens[t])

			n = int(class[2] - 48)

			if n > 0 {
				result = append(result, numbers[n])
			}
		}
	}

	// Add class name

	if index > 1 {
		result = append(result, classes[index])
	}
	return result
}

func joinSlices[T any](ss [][]T) []T {
	l := 0

	for i := range ss {
		l += len(ss[i])
	}

	s := make([]T, l)
	i := 0

	for y := range ss {
		for x := range ss[y] {
			s[i] = ss[y][x]
			i++
		}
	}
	return s
}

/*
Перетворює невід'ємне ціле число `num` на його представлення англійськими словами

	numberToWords(12_537) -> "Twelve Thousand Five Hundred Thirty Seven"
*/
func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}
	s := strconv.Itoa(num)

	// Add zeros to start

	zeros := 3 - (len(s) % 3)

	if zeros < 3 {
		s = strings.Repeat("0", zeros) + s
	}

	// convert classes to words

	parts := [][]string{}
	class := len(s) / 3

	for i := 0; i < len(s); i += 3 {
		parts = append(parts, classToWords(s[i:i+3], class))
		class--
	}

	words := joinSlices(parts)
	return strings.Join(words, " ")
}

func main() {
	println(numberToWords(27_371_865))
}
