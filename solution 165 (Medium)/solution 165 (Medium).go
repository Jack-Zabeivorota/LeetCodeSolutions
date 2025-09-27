package main

import (
	"strconv"
	"strings"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func parseVerion(v string, l int) []int {
	parts := strings.Split(v, ".")
	nums := make([]int, l)

	for i := range nums {
		if i < len(parts) {
			nums[i], _ = strconv.Atoi(parts[i])
		} else {
			nums[i] = 0
		}
	}
	return nums
}

/*
Порівнює версії формату `x.x.x`, де `x` це ціле число, та повертає:
  - 0 - якщо версії рівні
  - -1 - якщо version1 < version2
  - 1 - якщо version1 > version2
*/
func compareVersion(version1, version2 string) int {
	l := max(len(version1), len(version2))
	v1, v2 := parseVerion(version1, l), parseVerion(version2, l)

	for i := range v1 {
		if v1[i] < v2[i] {
			return -1
		}

		if v1[i] > v2[i] {
			return 1
		}
	}
	return 0
}

func main() {
	println(compareVersion("1.2", "1.7"))       // -> -1
	println(compareVersion("50.0", "50.0.0.0")) // -> 0
	println(compareVersion("0.01.0", "0.0001")) // -> 0
	println(compareVersion("1.2.0.0.3", "1.2")) // -> 1
}
