package main

func createMatrix(rows, columns int) [][]int {
	matrix := make([][]int, rows)

	for i := range matrix {
		matrix[i] = make([]int, columns)
	}
	return matrix
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func last[T any](arr []T) T {
	return arr[len(arr)-1]
}

/*
Повертає мінімальний час приготування зілль `potions` магами `wizards`.
  - Зілля потрібно приготувати послідовно.
  - Для створення одного зілля потрібно передавати його кожному магу послідовно.
  - Як тільки маг `i` закінчить свою часину приготування, його відразу потрібно передати магу `i+1`.
  - Час приготування зілля це `time[i] = potions[i] * wizards[j]`.

.

	println(minTime([]int{1,5,2,4}, []int{5,1,4,2})) -> 110

	// Potion | start      Wizards
	//    0	  | 0       5   30  40  60
	//    1	  | 52      53  58  60  64
	//    2	  | 54      58  78  86  102
	//    3	  | 86      88  98  102 110
*/
func minTime(wizards, potions []int) int64 {
	table := createMatrix(len(potions), len(wizards)+1)

	// set time in first row for first potion
	for j := range wizards {
		table[0][j+1] = table[0][j] + wizards[j]*potions[0]
	}

	for i := 1; i < len(table); i++ {
		// set start time
		table[i][0] = table[i-1][1]
		delta := 0

		// set time in current row and find time delta between
		// end of work current and next wizard
		for j := range wizards {
			table[i][j+1] = table[i][j] + wizards[j]*potions[i]
			delta = min(delta, table[i][j]-table[i-1][j+1])
		}

		// if delta is negative (wizards[i] has already done work, and
		// wizards[i+1] is still working), then add it to all times in the current row
		if delta < 0 {
			delta = -delta

			for j := range table[i] {
				table[i][j] += delta
			}
		}
	}
	return int64(last(last(table)))
}

func main() {
	println(minTime([]int{1, 5, 2, 4}, []int{5, 1, 4, 2})) // -> 110
	println(minTime([]int{1, 2, 3, 4}, []int{1, 2}))       // -> 21
}
