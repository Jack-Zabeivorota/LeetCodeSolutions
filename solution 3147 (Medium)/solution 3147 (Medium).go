package main

/*
Повертає максимальну кількість енергії, яку можно отримати за наступними правилами:
  - кожет тотем може додати або відняти певну кількість енергії.
  - після взаємодії з тотемом `i` потрібно перейти до тотему `i + k`,
  і так доки вони не скінчаться.
.
	maximumEnergy([]int{5, 2, -10, -5, 1, 8, 3, 10}, 3) -> 13

	//   +--------+-----+
	// 5 2 -10 -5 1 8 3 9
*/
func maximumEnergy(totems []int, k int) int {
	maxSum := -1000

	for i := len(totems) - k; i < len(totems); i++ {
		if totems[i] > maxSum {
			maxSum = totems[i]
		}
	}

	for i := len(totems) - k - 1; i >= 0; i-- {
		totems[i] += totems[i+k]

		if totems[i] > maxSum {
			maxSum = totems[i]
		}
	}
	return maxSum
}

func main() {
	println(maximumEnergy([]int{5, 2, -10, -5, 1, 8, 3, 10}, 3)) // -> 13
	println(maximumEnergy([]int{-2, -3, -1}, 2))                 // -> -1
}
