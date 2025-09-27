package main

import "slices"

/*
Повертає кількість трикутників, які можно утворити з ліній `lines`

	triangleNumber([]int{4, 3, 2, 2}) -> 3

	// 4,3,2 (using the first 2)
	// 4,3,2 (using the second 2)
	// 3,2,2
*/
func triangleNumber(lines []int) int {
	slices.SortFunc(lines, func(n1, n2 int) int {
		if n1 > n2 {
			return -1
		}
		if n1 < n2 {
			return 1
		}
		return 0
	})
	count := 0

	for i := 0; i < len(lines)-2; i++ {
		for j := i + 1; j < len(lines)-1; j++ {
			if lines[i] >= lines[j]+lines[j+1] {
				break
			}

			for k := j + 1; k < len(lines); k++ {
				if lines[i] >= lines[j]+lines[k] {
					break
				}
				count++
			}
		}
	}
	return count
}

func main() {
	println(triangleNumber([]int{2, 2, 3, 4})) // -> 3
	println(triangleNumber([]int{4, 2, 3, 4})) // -> 4
}
