package main

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

/*
Умови: квадрати падають послідовно, кожен з них зупиняється під час контакту
з іншим квадратом або віссю X.

`positions` описує квадрати `[left, side_length]`.
Квадрати падають в послідовності їх розташування в `positions`.

Функція повертає масив максимальних висот стопок квадратів після кожного падіння.

	6
	5   ######
	4   ######
	3   ######
	2 ####
	1 ####      ##
	0 1 2 3 4 5 6 7 8

	fallingSquares([1, 2], [2, 3], [6, 1]]) -> [2, 5, 5]
*/
func fallingSquares(positions [][]int) []int {
	heights := make([]int, len(positions))
	heights[0] = positions[0][1]

	max_hs := make([]int, len(positions))
	max_hs[0] = heights[0]

	for i := 1; i < len(positions); i++ {
		x1, side := positions[i][0], positions[i][1]
		x2 := x1 + side

		for j := 0; j < i; j++ {
			x1_, side_ := positions[j][0], positions[j][1]
			x2_ := x1_ + side_

			// if squares is crossed
			if !(x2 <= x1_ || x2_ <= x1) {
				heights[i] = max(heights[i], heights[j])
			}
		}

		heights[i] += side
		max_hs[i] = max(max_hs[i-1], heights[i])
	}

	return max_hs
}

func main() {
	fallingSquares([][]int{{1, 2}, {2, 3}, {6, 1}}) // -> [2, 5, 5]
	fallingSquares([][]int{{100, 100}, {200, 100}}) // -> [100, 100]
}
