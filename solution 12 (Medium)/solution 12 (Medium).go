package main

import (
	"fmt"
	"strconv"
	"strings"
)

func numToRanks(num int) []int {
	s := strconv.Itoa(num)
	ranks := make([]int, len(s))

	for i := range s {
		ranks[i], _ = strconv.Atoi(string(s[i]))
	}
	return ranks
}

/*
Конвертує десятичне число в римскі числа.
*/
func intToRoman(num int) string {
	ranks := []string{"I", "V", "X", "L", "C", "D", "M"}
	i := 0

	nums := numToRanks(num)
	res := make([]string, len(nums))

	for j := len(nums) - 1; j >= 0; j-- {
		num = nums[j]

		if i == 6 || num < 4 {
			res[j] = strings.Repeat(ranks[i], num)

		} else if num == 4 {
			res[j] = fmt.Sprint(ranks[i], ranks[i+1])

		} else if num < 9 {
			res[j] = fmt.Sprint(ranks[i+1], strings.Repeat(ranks[i], num-5))

		} else {
			res[j] = fmt.Sprint(ranks[i], ranks[i+2])
		}

		i += 2
	}

	return strings.Join(res, "")
}

func main() {
	println(intToRoman(18))   // -> XVIII
	println(intToRoman(134))  // -> CXXXIV
	println(intToRoman(2867)) // -> MMDCCCLXVII
}
